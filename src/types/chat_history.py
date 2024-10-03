class ChatHistory:
    def __init__(self, user_prompt: str, ai_prompt: str):
        self.user_prompt = user_prompt
        self.ai_prompt = ai_prompt

    def __getitem__(self, property):
          return self[property]