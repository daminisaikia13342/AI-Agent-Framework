from .base import BaseExecutor

class ToolExecutor(BaseExecutor):
    def execute(self, input_data, state):
        return input_data.strip().upper()
