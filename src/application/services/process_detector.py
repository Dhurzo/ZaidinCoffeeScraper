from abc import ABC, abstractmethod


class ProcessDetector(ABC):
    @abstractmethod
    def detect_process(self, text: str) -> str:
        pass
