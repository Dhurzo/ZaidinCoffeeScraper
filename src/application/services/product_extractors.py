from abc import ABC, abstractmethod
from typing import Any, List

from src.application.dtos.coffee_dtos import ProductBasicInfo


class ProductInfoExtractor(ABC):
    @abstractmethod
    async def extract_basic_info(self, product: Any) -> ProductBasicInfo:
        pass


class ProductDetailsExtractor(ABC):
    @abstractmethod
    async def extract_displayed_price(self, page: Any) -> str:
        pass

    @abstractmethod
    async def extract_formats(self, page: Any) -> List[str]:
        pass
