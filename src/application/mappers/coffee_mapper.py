from abc import ABC, abstractmethod

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.domain.entities.coffee import Coffee


class CoffeeMapper(ABC):
    """Abstract interface for coffee mapping operations"""

    @abstractmethod
    def to_entity(
        self, basic_info: ProductBasicInfo, details: ProductDetails
    ) -> Coffee | None:
        """Maps DTO objects to domain entity"""
        pass
