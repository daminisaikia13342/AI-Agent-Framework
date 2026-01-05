from .base import BaseExecutor

class OCRExecutor(BaseExecutor):
    def execute(self, input_data, state):
        return f"[OCR] Extracted text from document: {input_data}"
