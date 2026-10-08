from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.application.interfaces.logger import ILogger
from src.application.mappers.coffee_mapper import CoffeeMapper
from src.domain.entities.coffee import Coffee
from src.domain.entities.price import Price
from src.domain.exceptions.coffee_exceptions import PriceParsingError


class CoffeeMapperImpl(CoffeeMapper):
    def __init__(self, logger: ILogger):
        self._logger = logger

    def to_entity(
        self, basic_info: ProductBasicInfo, details: ProductDetails
    ) -> Coffee | None:
        try:
            format_text = details.formats[0] if details.formats else "250g"
            price = Price.from_text(basic_info.price_text, format_text)

            if not price:
                return None

            return Coffee(
                name=basic_info.name,
                price_per_kg=price.amount,
                process=details.process,
                formats=details.formats,
            )
        except PriceParsingError as e:
            self._logger.error(f"Error mapping coffee {basic_info.name}: {e.original}")
            return None
