from typing import Optional
from .chat_history import ChatHistory

class ChatCompletionRequest:
    def __init__(self, user_prompt: str, namespace_id: str, chat_history: list[ChatHistory], search_query: Optional[str]=None):
        self.user_prompt = user_prompt
        self.namespace_id = namespace_id
        self.chat_history = chat_history
        self.search_query = search_query