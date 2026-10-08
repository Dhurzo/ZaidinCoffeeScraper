from abc import ABC, abstractmethod
from typing import Any


class PageNavigator(ABC):
    @abstractmethod
    async def navigate_to_product(self, browser: Any, url: str) -> Any:
        pass
