from abc import ABC, abstractmethod

class BaseExecutor(ABC):
    @abstractmethod
    def execute(self, input_data, state):
        pass
