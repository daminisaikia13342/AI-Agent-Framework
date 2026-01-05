from .base import BaseExecutor

class LLMExecutor(BaseExecutor):
    def execute(self, input_data, state):
        return f"[LLM] Generated response based on: {input_data}"
