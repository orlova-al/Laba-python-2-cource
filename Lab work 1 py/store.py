import item
import provider
from dataclasses import asdict
from datetime import datetime, timedelta
from courier import Courier
from storekeeper import Storekeeper

id_product_store = []
id_product_store2 = []


class Store:
    __ip_store = 1
    __ip_store2 = 45
    __start1 = datetime.now() + timedelta(hours=0, seconds=0)
    __finish1 = datetime.now() + timedelta(hours=2, seconds=30)
    __start2 = datetime.now() + timedelta(hours=1, seconds=0)
    __finish2 = datetime.now() + timedelta(hours=4, seconds=20)

    @staticmethod
    def send_request():
        order_to_provider = []
        index = int(input("Enter number of count product: "))
        for i in range(index):
            n = str(input("Enter name of product: "))
            count = int(input("Enter count of product: "))
            order_to_provider.append(item.Item(0, 0, n, 0, count))
        p = provider.Provider()
        p.send_order(order_to_provider)




    def take_order(self, d, ip_user):
        count_time = timedelta(len(d) * 45 + 60 * max(abs(ip_user-self.__ip_store),
                                                      abs(ip_user-self.__ip_store2)) + 120)
        if self.__finish1 - self.__start1 + count_time:
            if abs(ip_user - self.__ip_store) <= abs(ip_user - self.__ip_store2):
                tmp = True
                order_for_user = []
                for i in range(len(d)):
                    for j in range(len(id_product_store)):
                        if asdict(d[i])['_Item__product_name'] == asdict(id_product_store[j])['_Item__product_name']:
                            if asdict(d[i])['_Item__count'] <= asdict(id_product_store[j])['_Item__count']:
                                order_for_user.append(d[i])
                            else:
                                order_for_user.append(id_product_store[j])
                                tmp = False
                if tmp:
                    self.get_worker(order_for_user, ip_user, self.__ip_store)

                else:
                    print("No item/ product")
                    tmp = True
                    if len(order_for_user) != 0:
                        while tmp:
                            s = str(input("Do you want delete order? Y/N "))
                            if s == "y" or s == "Y":
                                order_for_user.clear()
                                print("Order is deleted")
                                tmp = False
                            elif s == "n" or s == "N":
                                self.get_worker(order_for_user, ip_user, self.__ip_store)
                                tmp = False
                            else:
                                print("Incorrect input, try again")
                    else:
                        print("The order cannot be completed")
        elif self.__start2 + count_time <= self.__finish2:
            tmp = True
            order_for_user = []
            for i in range(len(d)):
                for j in range(len(id_product_store2)):
                    if asdict(d[i])['_Item__product_name'] == asdict(id_product_store2[j])['_Item__product_name']:
                        if asdict(d[i])['_Item__count'] <= asdict(id_product_store2[j])['_Item__count']:
                            order_for_user.append(id_product_store2[j])
                        else:
                            order_for_user.append(id_product_store[j])
                            tmp = False
            if tmp:
                self.get_worker(order_for_user, ip_user, self.__ip_store2)

            else:
                print("No item/ product")
                tmp = True
                if len(order_for_user) != 0:
                    while tmp:
                        s = str(input("Do you want delete order? Y/N "))
                        if s == "y" or s == "Y":
                            order_for_user.clear()
                            print("Order is deleted")
                            tmp = False
                        elif s == "n" or s == "N":
                            self.get_worker(order_for_user, ip_user, self.__ip_store2)
                            tmp = False

                        else:
                            print("Incorrect input, try again")
                else:
                    print("The order cannot be completed")

    # принять заказ и начать его обрабатывать
    def get_worker(self, order, a, ids):
        s = Storekeeper()
        c = Courier()
        tmp = False
        s1 = s.get_shift()
        c1 = c.get_shift()
        if s1 != -1 and c1 != -1:
            tmp = True
        else:
            print("The order cannot be accepted")
        if tmp:
            order1 = self.set_storekeeper(order, a, s1, ids)

            self.set_courier(order1, a, c1, ids)




    @staticmethod
    def set_courier(order, ip_user, idc, ids):
        c = Courier()
        c.get_order(order, ip_user, idc, ids)
    # дать заказу курьера


    @staticmethod
    def set_storekeeper(order, ip_user, idsk, ids):
        s = Storekeeper()
        return s.get_order(order, ip_user, idsk, ids)
