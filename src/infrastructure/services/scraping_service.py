from typing import Any, List

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.application.interfaces.logger import ILogger
from src.application.services.element_finder import ElementFinder
from src.application.services.page_navigator import PageNavigator
from src.application.services.process_detector import ProcessDetector
from src.application.services.product_extractors import (
    ProductDetailsExtractor,
    ProductInfoExtractor,
)
from src.application.services.scraping_service import (
    ProductCollector,
    ProductDetailCollector,
    ScrapingServiceInterface,
)


class ProductCollectorImpl(ProductCollector):
    def __init__(
        self,
        product_info_extractor: ProductInfoExtractor,
        element_finder: ElementFinder,
        logger: ILogger,
    ):
        self._product_info_extractor = product_info_extractor
        self._element_finder = element_finder
        self._logger = logger

    async def collect_products(self, page: Any) -> List[ProductBasicInfo]:
        products = []
        product_elements = await self._element_finder.find_product_elements(page)

        for element in product_elements:
            try:
                product_info = await self._product_info_extractor.extract_basic_info(
                    element
                )
                if product_info:
                    products.append(product_info)
            except Exception as e:
                self._logger.error(f"Error extracting product info: {str(e)}")
                continue
        return products


class ProductDetailCollectorImpl(ProductDetailCollector):
    def __init__(
        self,
        product_details_extractor: ProductDetailsExtractor,
        page_navigator: PageNavigator,
        process_detector: ProcessDetector,
    ):
        self._product_details_extractor = product_details_extractor
        self._page_navigator = page_navigator
        self._process_detector = process_detector

    async def collect_details(self, browser: Any, href: str) -> ProductDetails:
        page = await self._page_navigator.navigate_to_product(browser, href)
        try:
            details = await self._product_details_extractor.extract(page)
            desc_el = await page.query_selector("#productDescription")
            if desc_el:
                description = await desc_el.inner_text()
                detected_process = self._process_detector.detect_process(description)
                details.process = detected_process
            return details
        finally:
            await page.close()


class ScrapingService(ScrapingServiceInterface):
    def __init__(
        self,
        product_collector: ProductCollector,
        detail_collector: ProductDetailCollector,
    ):
        self._product_collector = product_collector
        self._detail_collector = detail_collector

    async def get_products(self, page: Any) -> List[ProductBasicInfo]:
        return await self._product_collector.collect_products(page)

    async def extract_detail_info(self, browser: Any, href: str) -> ProductDetails:
        return await self._detail_collector.collect_details(browser, href)
