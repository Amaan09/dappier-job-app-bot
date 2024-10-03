# AI Interview Assistant with RAG Model

This project is an AI-powered interview assistant that utilizes Retrieval-Augmented Generation (RAG) models to generate dynamic interview questions based on a user's resume and job description. It supports custom chat interactions, history tracking, and multi-modal search through different documents.

## Features

-   **OpenAI API Integration**: Utilizes OpenAI's API for embedding and completion tasks.
-   **Pinecone DB**: A vector database to store and search embeddings efficiently.
-   **RAG Model**: Dynamic AI chat completion using Retrieval-Augmented Generation.
-   **Chat History**: Tracks previous user prompts and AI responses to avoid repetitive questions.
-   **Multi-Modal Search**: Search across multiple documents like resumes, job descriptions, or both.
-   **Namespaces and Metadata**: Dynamically create namespaces for each user and utilize metadata for specific document searches.
