import re
from dataclasses import dataclass
from typing import Optional

from src.domain.exceptions.coffee_exceptions import PriceParsingError


@dataclass(frozen=True)
class Price:
    amount: float
    weight_grams: int = 250

    @classmethod
    def from_text(cls, price_text: str, format_text: str) -> Optional["Price"]:
        try:
            clean = price_text.strip().replace("€", "")
            if "," in clean and "." not in clean:
                clean = clean.replace(",", ".")
            price_match = re.search(r"(\d+[.,]?\d*)", clean)
            if not price_match:
                raise ValueError(f"Not price found in {clean}")

            base_price = float(price_match.group(1))

            weight_match = re.search(r"(\d+)\s*g", format_text)
            if weight_match:
                weight_grams = int(weight_match.group(1))
            else:
                weight_grams = 250

            price_per_kg = (base_price / weight_grams) * 1000

            return cls(amount=price_per_kg, weight_grams=weight_grams)
        except Exception as e:
            raise PriceParsingError(price_text, format_text, e)

    @property
    def price_per_kg(self) -> float:
        return self.amount

    def __str__(self) -> str:
        return f"{self.amount:.2f}€/kg"
