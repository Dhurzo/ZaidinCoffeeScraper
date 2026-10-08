from abc import ABC, abstractmethod
from typing import List, Any


class ElementFinder(ABC):
    @abstractmethod
    async def find_product_elements(self, page: Any) -> List[Any]:
        pass
