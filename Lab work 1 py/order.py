from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    __status_delivery: str
    __list_of_product: []
    __time_first: datetime
    __time_second: datetime
    __who_send: str
