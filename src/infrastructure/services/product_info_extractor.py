from typing import Any

from src.application.dtos.coffee_dtos import ProductBasicInfo
from src.application.services.product_extractors import ProductInfoExtractor


class WebProductInfoExtractor(ProductInfoExtractor):
    async def extract_basic_info(self, product: Any) -> ProductBasicInfo:
        name_el = await product.query_selector(".grid-product__title-inner")
        price_el = await product.query_selector(".grid-product__price-value")
        link_el = await product.query_selector("a.grid-product__title")

        name = await name_el.inner_text() if name_el else "Unknown"
        price = await price_el.inner_text() if price_el else ""
        href = await link_el.get_attribute("href") if link_el else None

        return ProductBasicInfo(name=name.strip(), price_text=price.strip(), href=href)
