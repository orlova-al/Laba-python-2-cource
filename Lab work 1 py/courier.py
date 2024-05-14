from datetime import datetime, timedelta
import time
from order import Order
from worker import Worker


class Courier(Worker):
    __name_courier = [{'Name': 'Ivan', 'Status': 'Free', 'Start_s': datetime.now() + timedelta(seconds=0), 'Salary': 0},
                      {'Name': 'Roman', 'Status': 'Free', 'Start_s': datetime.now() + timedelta(seconds=0),
                       'Salary': 0}]

    def get_shift(self):
        a = -1
        if self.__name_courier[0]['Status'] == 'Free':
            print("The courier is assigned: " + self.__name_courier[0]['Name'])
            self.__name_courier[0].update({'Status': 'Busy'})
            self.__name_courier[0].update({'Start_s': datetime.now() + timedelta(seconds=0)})
            a = 0
        elif self.__name_courier[1]["Status"] == 'Free' and a == -1:
            print("The courier is assigned: " + self.__name_courier[1]['Name'])
            self.__name_courier[1].update({'Status': 'Busy'})
            self.__name_courier[1].update({'Start_s': datetime.now() + timedelta(seconds=0)})
            a = 1
        return a


    def get_name_courier(self, num):
        return self.__name_courier[num]['Name']


    def get_order(self, order, a, num, ids):
        times = timedelta(seconds=120 + abs(ids - a) * 30)
        start = self.__name_courier[num]['Start_s']
        o = Order("Delivery", order, start, start + timedelta(times.seconds), self.get_name_courier(num))
        time.sleep(5)
        self.__name_courier[num]['Salary'] += 300 * (120 + abs(ids - a) * 30) / 3600
        print("Salary per order " + self.get_name_courier(num))
        print(self.__name_courier[num]['Salary'])
        self.__name_courier[num]['Status'] = 'Free'
        print("Delivery to user")
        return o
