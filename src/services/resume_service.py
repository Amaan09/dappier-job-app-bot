import itertools
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from werkzeug.exceptions import NotFound, BadRequest
from ..types import TrainModelRequest, TrainModelResponse, ChatCompletionRequest, ChatCompletionResponse
from ..config import resume_index, openai_model, resume_system_prompt

def train_model(request: TrainModelRequest):
    namespace_id = _generate_namespace_id(request=request)

    # If namespace already exists, return with bad request.
    if _namespace_exists(namespace_id=namespace_id):
        raise BadRequest("Namespace already exists.")
    
    # Create documents with both Job description and Resume for RAG.
    documents = _create_documents(request=request)

    # Create a vector store.
    vector_store = PineconeVectorStore(index=resume_index, embedding=OpenAIEmbeddings(), namespace=namespace_id)

    # Insert documents into vector store.
    vector_store.add_documents(documents=documents)
    
    return TrainModelResponse(status="success", namespace_id=namespace_id)


def chat_completion(request: ChatCompletionRequest):

    #If namespace doesnot exist, return an exception.
    if not _namespace_exists(namespace_id=request.namespace_id):
        raise NotFound("Namespace does not exist.")
    
    # Create chat completion prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", resume_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    # Get the vector store
    vector_store = PineconeVectorStore(index=resume_index, embedding=OpenAIEmbeddings(), namespace=request.namespace_id)
    
    # Create retriver from the vector store.
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs = _get_search_kwargs(request=request)
    )

    # Create RAG chain
    question_answer_chain = create_stuff_documents_chain(openai_model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Call the embedded model.
    response = rag_chain.invoke({
        "input": request.user_prompt,
        "chat_history": _build_chat_history(request=request)
    })

    return ChatCompletionResponse(user_prompt=response["input"], ai_prompt=response["answer"], namespace_id=request.namespace_id)


def _build_chat_history(request: ChatCompletionRequest):
    chat_history = []
    for history in request.chat_history:
        chat_history.append(HumanMessage(content=history['user_prompt']))
        chat_history.append(AIMessage(content=history['ai_prompt']))
    return chat_history


def _get_search_kwargs(request: ChatCompletionRequest):
    search_kwargs={ }
    if request.search_query:
        search_kwargs = { "filter": {"type": {"$eq": request.search_query}} }
    return search_kwargs


def _namespace_exists(namespace_id: str):
    namespaces = resume_index.describe_index_stats()['namespaces']
    return namespace_id in namespaces

def _create_documents(request: TrainModelRequest):
    # Create a text splitter with 1000 characters chunk size with 200 overlap.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    # Load resume docs
    loader = PyPDFLoader(request.resume_filepath)
    docs = loader.load()
    for doc in docs:
        doc.metadata["type"] = "resume"
    resume_docs = text_splitter.split_documents(docs)

    # Load Job description docs
    jd_docs = []
    for chunk in text_splitter.split_text(request.job_description):
        jd_docs.append(Document(page_content=chunk, metadata={"source": "text", "type": "job_description"}))

    return list(itertools.chain(jd_docs, resume_docs))


def _generate_namespace_id(request: TrainModelRequest):
    username = request.user_email.split('@')[0]
    return f"{username}_{request.resume_id}"