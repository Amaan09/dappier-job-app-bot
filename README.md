# Dappier Job Application Bot

## Overview

The Dappier Job Application Bot is a RAG (Retrieve and Generate) model service built to process user-uploaded resumes and job descriptions, providing insightful feedback and generating potential interview questions. This service integrates with the Dappier Job Application API to enhance the application's capabilities by handling the core natural language processing tasks.

## Features

- **Model Processing:** Utilizes advanced RAG models to process text data and generate feedback.
- **Customizable Prompts:** Allows configuration of system prompts for various use cases.
- **Integration Ready:** Designed to integrate seamlessly with other parts of the Dappier system.

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

   Run the script to start the service:

   ```bash
   flask --app src run --debug
   ```

2. **API Interaction:**

   Use the API endpoints configured in `src/routes/resume.py` to handle requests from other system components for processing resumes and generating output.

3. **Testing and Development:**

   Adjust the model parameters and prompts in configuration files as necessary to refine results or adapt to new requirements.

---

This project is an integral part of the Dappier Job Application system, working alongside the [Dappier Job Application API](https://github.com/Amaan09/dappier-job-app-api) and the [Dappier Job Application UI](https://github.com/Amaan09/dappier-job-app-ui).
```
