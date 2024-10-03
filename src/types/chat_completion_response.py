class ChatCompletionResponse:
    def __init__(self, user_prompt: str, ai_prompt: str, namespace_id: str):
        self.user_prompt = user_prompt
        self.ai_prompt = ai_prompt
        self.namespace_id = namespace_id

    def to_dict(self) -> dict:
        return {
            "user_prompt": self.user_prompt,
            "ai_prompt": self.ai_prompt,
            "namespace_id": self.namespace_id
        }
