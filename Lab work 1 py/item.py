from dataclasses import dataclass


@dataclass
class Item:
    __id_store: int
    __id_provider: int
    __product_name: str
    __price: int
    __count: int
