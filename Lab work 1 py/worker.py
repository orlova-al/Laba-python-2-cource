import abc
from datetime import datetime


class Worker(abc.ABC):
    __start_shift: datetime
    __finish_shift: datetime
    __salary: int
    __order_num: int

    @abc.abstractmethod
    def get_order(self, order, a, name, ids):
        pass

    # принять заказ, если возможно

    # режим админ назанчить смену работникам

    @abc.abstractmethod
    def get_shift(self):
        pass
