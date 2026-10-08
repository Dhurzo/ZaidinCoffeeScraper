from abc import ABC, abstractmethod
from typing import Any, List

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails


class ScrapingServiceInterface(ABC):
    @abstractmethod
    async def get_products(self, page: Any) -> List[Any]:
        """Get all products from page"""
        pass


class ProductCollector(ABC):
    @abstractmethod
    async def collect_products(self, page: Any) -> List[ProductBasicInfo]:
        pass


class ProductDetailCollector(ABC):
    @abstractmethod
    async def collect_details(self, browser: Any, href: str) -> ProductDetails:
        pass
