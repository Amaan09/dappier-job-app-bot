# Dappier Job Application Bot

## Overview

The Dappier Job Application Bot is a cutting-edge RAG (Retrieve and Generate) model service engineered to process user-uploaded resumes and job descriptions. It provides insightful feedback and generates potential interview questions to enhance the application experience. This service is seamlessly integrated with the Dappier Job Application API, handling core natural language processing tasks with precision and efficiency.

## Features

- **Advanced Model Processing:** Leverages state-of-the-art RAG models to process text data effectively, offering users tailored feedback and suggestions.
- **Customizable Prompts:** Users can configure system prompts to suit various use cases, providing a personalized interaction experience.
- **OpenAI Integration:** Utilizes OpenAIEmbeddings, supported by an Open AI account setup for token usage, to enhance text processing capabilities.
- **Flask Project Structure:** The backend is structured using Flask, ensuring robust and scalable route and service management.
- **API Key Security:** Environment variables securely store API keys, maintaining the integrity of user data.
- **RAG Model Interaction:** Features a dedicated route for chat completion with the RAG model and an initial model training route.
- **Pinecone Vector Database:** Implements Pinecone as a vector database to efficiently handle and search large datasets.
- **Dynamic Embeddings and Indexes:** Processes raw data into vector embeddings, creating dynamic indexes and namespaces tailored for individual users and resumes.
- **Metadata-Driven Search:** Employs metadata to refine searches within vector datasets, targeting either resumes or job descriptions.
- **User-Specific Namespaces:** Constructs unique namespaces for different users based on uploaded resumes, ensuring organized data management.
- **Chat History Tracking:** Maintains chat history to facilitate diverse question generation and minimize repetitive feedback.
- **Multi-modal Search Capabilities:** Supports searching across multiple document types, such as resumes and job descriptions, simultaneously.
- **Heroku Deployment:** The Flask application is deployed on Heroku, ensuring reliable and scalable application access.

With these comprehensive features, the Dappier Job Application Bot is equipped to deliver exceptional user support and enhance the job application process through intelligent text analysis and feedback mechanisms.

## Project Structure

```plaintext
src
├── __init__.py
├── config
│   ├── __init__.py
│   ├── open_ai.py
│   ├── pinecone_db.py
│   └── system_prompts.py
├── routes
│   ├── __init__.py
│   └── resume.py
├── services
│   ├── __init__.py
│   └── resume_service.py
└── types
    ├── __init__.py
    ├── chat_completion_request.py
    ├── chat_completion_response.py
    ├── chat_history.py
    ├── train_model_request.py
    └── train_model_response.py
```

## Getting Started

Follow the instructions below to set up and run the Dappier Job Application Bot service on your local machine.

## Prerequisites

Ensure you have the following software installed:

- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Amaan09/dappier-job-app-bot.git
   cd dappier-job-app-bot
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration:**

   Create a `.env` file in the root directory and populate it with the following variables:

   ```plaintext
   # LANGSMITH
   LANGCHAIN_TRACING_V2=
   LANGCHAIN_API_KEY=
   USER_AGENT=

   # OPEN_AI
   OPENAI_API_KEY=
   OPENAI_MODEL=

   # VECTOR_DB
   PINECONE_API_KEY=
   RESUME_INDEX_NAME=

   # API_SECRET
   DAPPIER_BOT_API_SECRET=
   ```

   Ensure your configuration files (`open_ai.py`, `pinecone_db.py`, and `system_prompts.py`) are set up to connect to the required services using these environment variables.

## Usage

1. **Start the Service:**

   Run the script to start the development server:

   ```bash
   flask --app src run --debug
   ```

   Run the script to start the production server:

   ```bash
   gunicorn src:app
   ```

3. **API Interaction:**

   Use the API endpoints configured in `src/routes/resume.py` to handle requests from other system components for processing resumes and generating output.

4. **Testing and Development:**

   Adjust the model parameters and prompts in configuration files as necessary to refine results or adapt to new requirements.

---

This project is an integral part of the Dappier Job Application system, working alongside the [Dappier Job Application API](https://github.com/Amaan09/dappier-job-app-api) and the [Dappier Job Application UI](https://github.com/Amaan09/dappier-job-app-ui).
