from typing import Any, List

from src.application.services.element_finder import ElementFinder
from src.domain.configuration.scraping_config import ScrapingConfig


class WebElementFinder(ElementFinder):
    def __init__(self, config: ScrapingConfig):
        self._config = config

    async def find_product_elements(self, page: Any) -> List[Any]:
        for selector in self._config.get_product_selectors():
            try:
                await page.wait_for_selector(selector, timeout=2000)
                products = await page.query_selector_all(selector)
                if products:
                    return products
            except Exception:
                continue
        return []
