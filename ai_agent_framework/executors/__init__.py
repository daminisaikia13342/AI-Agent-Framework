from .llm_executor import LLMExecutor
from .ocr_executor import OCRExecutor
from .tool_executor import ToolExecutor

EXECUTORS = {
    "llm": LLMExecutor(),
    "ocr": OCRExecutor(),
    "tool": ToolExecutor()
}
