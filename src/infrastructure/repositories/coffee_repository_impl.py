import asyncio
from typing import List

from src.domain.entities.coffee import Coffee
from src.domain.exceptions.coffee_exceptions import CoffeeScrapingError
from src.domain.repositories.coffee_repository import CoffeeRepository
from src.infrastructure.mappers.coffee_mapper import CoffeeMapper
from src.infrastructure.services.coffee_scraper import CoffeeScraper


class CoffeeRepositoryImpl(CoffeeRepository):
    MAX_CONCURRENT_PRODUCT_PAGES = 4

    def __init__(
        self,
        coffee_scraper: CoffeeScraper,
        coffee_mapper: CoffeeMapper,
    ):
        self._scraper = coffee_scraper
        self._mapper = coffee_mapper

    async def fetch_by_category(self, category_url: str) -> List[Coffee]:
        try:
            async with self._scraper:
                products = await self._scraper.scrape_category(category_url)
                semaphore = asyncio.Semaphore(self.MAX_CONCURRENT_PRODUCT_PAGES)

                async def fetch_coffee(product):
                    if product.name.startswith(".Vale") or not product.href:
                        return None
                    async with semaphore:
                        details = await self._scraper.scrape_details(product.href)
                    return self._mapper.to_entity(product, details)

                results = await asyncio.gather(
                    *(fetch_coffee(product) for product in products)
                )
                return [coffee for coffee in results if coffee]
        except Exception as e:
            raise CoffeeScrapingError(
                f"Error fetching category {category_url}: {str(e)}"
            )
