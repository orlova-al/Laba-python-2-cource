
import item
import user
import store
from dataclasses import asdict


class Provider:

    def send_order(self, order):
        num_store = int(input("Enter num of store: "))
        order_to_store = []
        order_to_store2 = []
        if num_store == 1:
            for index in range(len(order)):
                for jx in range(len(user.id_product)):
                    if (asdict(order[index])['_Item__product_name'] ==
                            asdict(user.id_product[jx])['_Item__product_name']):
                        if asdict(order[index])['_Item__count'] <= asdict(user.id_product[jx])['_Item__count']:
                            order_to_store.append(order[index])
                            user.id_product[jx] = item.Item(asdict(user.id_product[jx])['_Item__id_store'],
                                                            asdict(user.id_product[jx])['_Item__id_provider'],
                                                            asdict(user.id_product[jx])['_Item__product_name'],
                                                            asdict(user.id_product[jx])['_Item__price'], abs(asdict(
                                                                    order[index])['_Item__count']
                                                                         - asdict(user.id_product[jx])['_Item__count']))

                            order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0, 0)


                        else:
                            tmp = True
                            for jxx in range(len(user.id_product2)):
                                if (asdict(order[index])['_Item__product_name'] ==
                                        asdict(user.id_product2[jx])['_Item__product_name']):
                                    tmp = False
                                    a = asdict(order[index])['_Item__count']
                                    b = asdict(user.id_product[jx])['_Item__count']
                                    if a - b <= asdict(user.id_product2[jx])['_Item__count']:
                                        order_to_store.append(order[index])
                                        user.id_product[jx] = item.Item(
                                            asdict(user.id_product[jx])['_Item__id_store'],
                                            asdict(user.id_product[jx])['_Item__id_provider'],
                                            asdict(user.id_product[jx])['_Item__product_name'],
                                            asdict(user.id_product[jx])['_Item__price'], 0)
                                        user.id_product2[jxx] = item.Item(
                                            asdict(user.id_product2[jxx])['_Item__id_store'],
                                            asdict(user.id_product2[jxx])['_Item__id_provider'],
                                            asdict(user.id_product2[jxx])['_Item__product_name'],
                                            asdict(user.id_product2[jxx])['_Item__price'],
                                            a - b)

                                        order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'],
                                                                 0, 0)
                                    else:
                                        order_to_store.append(order[index])
                                        l_o = len(order_to_store)
                                        order_to_store[l_o - 1] = item.Item(0, 0,
                                                                            asdict(order[index])['_Item__product_name'],
                                                                            0, user.id_product[jx][
                                                                                         '_Item__count'] +
                                                                            user.id_product[jxx][
                                                                                         '_Item__count'])
                            if tmp:
                                order_to_store.append(user.id_product[jx])
                                order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0,
                                                         abs(asdict(order[index])['_Item__count'] -
                                                             asdict(user.id_product[jx])['_Item__count']))
                                user.id_product[jx] = item.Item(
                                    asdict(user.id_product[jx])['_Item__id_store'],
                                    asdict(user.id_product[jx])['_Item__id_provider'],
                                    asdict(user.id_product[jx])['_Item__product_name'],
                                    asdict(user.id_product[jx])['_Item__price'], 0)
                    for jxx in range(len(user.id_product2)):
                        if (asdict(order[index])['_Item__product_name'] ==
                                asdict(user.id_product2[jxx])['_Item__product_name']):
                            if asdict(order[index])['_Item__count'] <= asdict(user.id_product2[jxx])['_Item__count']:
                                order_to_store.append(order[index])
                                user.id_product2[jxx] = item.Item(asdict(user.id_product2[jxx])['_Item__id_store'],
                                                                  asdict(user.id_product2[jxx])['_Item__id_provider'],
                                                                  asdict(user.id_product2[jxx])['_Item__product_name'],
                                                                  asdict(user.id_product2[jxx])['_Item__price'], abs
                                                                  (asdict(
                                                                        order[index])['_Item__count'] -
                                                                   asdict(user.id_product2[jxx])['_Item__count']))

                                order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0, 0)
                            else:
                                order_to_store.append(user.id_product2[jxx])

            self.update_stocks(order_to_store, 1)
            order_to_store.clear()


        if num_store == 2:
            for index in range(len(order)):
                for jx in range(len(user.id_product)):
                    if (asdict(order[index])['_Item__product_name'] ==
                            asdict(user.id_product[jx])['_Item__product_name']):
                        if asdict(order[index])['_Item__count'] <= asdict(user.id_product[jx])['_Item__count']:
                            order_to_store2.append(order[index])
                            user.id_product[jx] = item.Item(asdict(user.id_product[jx])['_Item__id_store'],
                                                            asdict(user.id_product[jx])['_Item__id_provider'],
                                                            asdict(user.id_product[jx])['_Item__product_name'],
                                                            asdict(user.id_product[jx])['_Item__price'], abs(asdict(
                                                                order[index])['_Item__count']
                                                                                                             - asdict(
                                                                        user.id_product[jx])['_Item__count']))

                            order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0, 0)
                            print(order[index])
                            print(user.id_product[jx])



                        else:

                            for jxx in range(len(user.id_product2)):
                                if (asdict(order[index])['_Item__product_name'] ==
                                        asdict(user.id_product2[jx])['_Item__product_name']):
                                    a = asdict(order[index])['_Item__count']
                                    b = asdict(user.id_product[jx])['_Item__count']
                                    if a - b <= asdict(user.id_product2[jx])['_Item__count']:
                                        order_to_store2.append(order[index])
                                        user.id_product[jx] = item.Item(
                                            asdict(user.id_product[jx])['_Item__id_store'],
                                            asdict(user.id_product[jx])['_Item__id_provider'],
                                            asdict(user.id_product[jx])['_Item__product_name'],
                                            asdict(user.id_product[jx])['_Item__price'], 0)
                                        user.id_product2[jxx] = item.Item(
                                            asdict(user.id_product2[jxx])['_Item__id_store'],
                                            asdict(user.id_product2[jxx])['_Item__id_provider'],
                                            asdict(user.id_product2[jxx])['_Item__product_name'],
                                            asdict(user.id_product2[jxx])['_Item__price'],
                                            a - b)

                                        order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'],
                                                                 0, 0)
                                    else:
                                        order_to_store2.append(order[index])
                                        l_o = len(order_to_store2)
                                        order_to_store2[l_o - 1] = item.Item(0, 0, asdict(order[index])
                                                                             ['_Item__product_name'], 0,
                                                                             user.id_product[jx][
                                                                                 '_Item__count'] +
                                                                             user.id_product[jxx][
                                                                                 '_Item__count'])

                            order_to_store.append(user.id_product[jx])
                            order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0,
                                                     abs(asdict(order[index])['_Item__count'] -
                                                         asdict(user.id_product[jx])['_Item__count']))
                    for jxx in range(len(user.id_product2)):
                        if (asdict(order[index])['_Item__product_name'] ==
                                asdict(user.id_product2[jxx])['_Item__product_name']):
                            if asdict(order[index])['_Item__count'] <= asdict(user.id_product2[jxx])['_Item__count']:
                                order_to_store.append(order[index])
                                user.id_product2[jxx] = item.Item(asdict(user.id_product2[jxx])['_Item__id_store'],
                                                                  asdict(user.id_product2[jxx])['_Item__id_provider'],
                                                                  asdict(user.id_product2[jxx])['_Item__product_name'],
                                                                  asdict(user.id_product2[jxx])['_Item__price'], abs
                                                                  (asdict(
                                                                        order[index])['_Item__count'] -
                                                                   asdict(user.id_product2[jxx])['_Item__count']))

                                order[index] = item.Item(0, 0, asdict(order[index])['_Item__product_name'], 0, 0)
                            else:
                                order_to_store.append(user.id_product2[jxx])
            self.update_stocks(order_to_store2, 2)
            order_to_store2.clear()



    @staticmethod
    def update_stocks(order_to_store, num):
        if num == 1:
            index = 0
            while index < len(order_to_store):
                store.id_product_store.append(order_to_store[index])
                index += 1
        if num == 2:
            index = 0
            while index < len(order_to_store):
                store.id_product_store2.append(order_to_store[index])
                index += 1
        if num > 2:
            print("Incorrect number of store")
