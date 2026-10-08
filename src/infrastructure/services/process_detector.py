import re

from src.application.services.process_detector import ProcessDetector


class CoffeeProcessDetector(ProcessDetector):
    def __init__(self):
        pass

    def detect_process(self, text: str) -> str:
        process_match = re.search(r"Proceso:\s*([^,.;\n]+)", text, re.IGNORECASE)
        if process_match:
            return process_match.group(1).strip()

        text_lower = text.lower()
        processes = {
            "natural": "Natural",
            "honey": "Honey",
            "lavado": "Lavado",
            "washed": "Washed",
            "fermentado": "Fermentado",
            "cofermentado": "Cofermentado",
        }

        for key, value in processes.items():
            if key in text_lower:
                return value
        return "Unknown"
