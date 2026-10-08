from dataclasses import dataclass


@dataclass(frozen=True)
class Coffee:
    name: str
    price_per_kg: float
    process: str
    formats: list[str]
