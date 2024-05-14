import random
from datetime import datetime, timedelta
import time

from order import Order
from worker import Worker


class Storekeeper(Worker):
    __name_storekeeper = [{'Name': 'Oleg', 'Status': 'Free', 'Start_s': datetime.now() + timedelta(seconds=0),
                           'Salary': 0},
                          {'Name': 'Boris', 'Status': 'Free', 'Start_s': datetime.now() + timedelta(seconds=0),
                           'Salary': 0}]


    def get_shift(self):
        tmp = -1
        if self.__name_storekeeper[0]['Status'] == 'Free':
            print("The storekeeper is assigned: " + self.__name_storekeeper[0]['Name'])
            self.__name_storekeeper[0].update({'Status': 'Busy'})
            self.__name_storekeeper[0].update({'Start_s': datetime.now() + timedelta(seconds=0)})
            tmp = 0
        elif self.__name_storekeeper[1]["Status"] == 'Free' and tmp == -1:
            print("The storekeeper is assigned: " + self.__name_storekeeper[1]['Name'])
            self.__name_storekeeper[1].update({'Status': 'Busy'})
            self.__name_storekeeper[1].update({'Start_s': datetime.now() + timedelta(seconds=0)})
            tmp = 1
        return tmp

    def get_name_storekeeper(self, num):
        return self.__name_storekeeper[num]['Name']



    def get_order(self, order, a, num, ids):
        times = timedelta(seconds=len(order) * 45)
        start = self.__name_storekeeper[num]['Start_s']
        o = Order("Accept", order, start, start + timedelta(times.seconds), self.get_name_storekeeper(num))
        print("Accept")
        time.sleep(10)
        print("Take to courier")
        k = len(order)
        self.__name_storekeeper[num]['Salary'] += 300 * k * 45 / 3600
        print("Salary per order " + self.get_name_storekeeper(num))
        print(self.__name_storekeeper[num]['Salary'])
        self.__name_storekeeper[num]['Status'] = 'Free'
        return o
