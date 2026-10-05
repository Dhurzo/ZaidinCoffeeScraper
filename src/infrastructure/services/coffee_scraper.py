from typing import List
from urllib.parse import urljoin

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.application.interfaces.logger import ILogger
from src.application.services.coffee_scraper import CoffeeScraper
from src.application.services.web_client import Browser, WebClient
from src.infrastructure.services.scraping_service import ScrapingService


class CoffeeScraper(CoffeeScraper):
    def __init__(
        self,
        web_client: WebClient,
        scraping_service: ScrapingService,
        logger: ILogger,
        base_url: str,
    ):
        self._web_client = web_client
        self._scraping_service = scraping_service
        self._logger = logger
        self._base_url = base_url
        self._browser: Browser | None = None

    async def __aenter__(self):
        await self._web_client.__aenter__()
        self._browser = await self._web_client.get_browser()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self._web_client.__aexit__(exc_type, exc_val, exc_tb)
        finally:
            self._browser = None

    async def scrape_category(self, url: str) -> List[ProductBasicInfo]:
        page = await self._web_client.new_page()
        try:
            await self._web_client.goto(page, url)
            products = await self._scraping_service.get_products(page)
            self._logger.info(
                f"Found {len(products)} products in category {url}... scraping details..."
            )
            return products
        finally:
            await self._web_client.close_page(page)

    async def scrape_details(self, url: str) -> ProductDetails:
        full_url = urljoin(self._base_url, url)
        if self._browser is None:
            raise RuntimeError("Coffee scraper must be used inside an async context")
        return await self._scraping_service.extract_detail_info(
            self._browser, full_url
        )
