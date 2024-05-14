import store
import item



name_of_client = []
id_product = []
id_product2 = []
name_of_product = [{}]


class User:
    __name: str
    __address: int


    def __init__(self, name1, address1):
        self.__name = name1
        self.__address = address1

    def login(self):
        tp = input("Admin/User [A/U] : ")
        if tp == 'A' or tp == 'a':
            password = input("Enter the password : ")
            if password == "123":
                self.admin_login()
            else:
                print("Invalid password. Please enter valid password")
        elif tp == 'U' or tp == 'u':
            self.user_login()
        else:
            print("Invalid user type. Enter valid user type")

    def admin_login(self):
        print("*********************")
        print("1.Add item for provider")
        print("2.Make an order for provider")
        print("3.Logout")
        print("*********************")
        choice = int(input("Enter number of menu: "))
        if choice == 1:
            self.add_item()
        if choice == 3:
            self.login()
        if choice == 2:
            s = store.Store()
            s.send_request()
            self.login()
        if choice > 3:
            print("Incorrect input")

    def user_login(self):
        print("*********************\n")
        print("1.Registration")
        print("2.Take order")
        print("3.Logout")
        print("\n*********************")
        choice = int(input("Enter number of menu: "))
        if choice == 1:
            print("Enter name: ")
            name = str(input())
            print("Enter address:  ")
            address = int(input())
            if address > 100:
                print("Incorrect address")
            else:
                name_of_client.append(name)
                print("OK")
                u = User(name, address)
                u.user_login()
                print("\n")


        if choice == 2:
            if len(name_of_client) > 0:
                self.make_order()
            else:
                print("Choice 1 before choice 2")
                self.user_login()

        if choice == 3:
            print("Thank you! See again!!!")
        elif choice > 3:
            print("Incorrect input")

    def add_item(self):
        id_provider = int(input("Enter number of provider: "))
        if id_provider == 1:
            n = int(input("Enter the count items need to be added: "))
            for i in range(n):
                new_ids = int(input("Enter id_store: "))
                new_idp = int(input("Enter id_provider: "))
                new_names = str(input("Enter Name: "))
                new_price = int(input("Enter Price: "))
                new_count = int(input("Enter Count: "))
                id_product.append(item.Item(new_idp, new_ids, new_names, new_price, new_count))
                print("Add item")
                a = {"ID": new_ids, "Name": new_names, "Price": new_price}
                if a not in name_of_product:
                    name_of_product.append(a)
            self.admin_login()
        elif id_provider == 2:
            n = int(input("Enter the no.of.items need to be added : "))
            for i in range(n):
                new_ids = int(input("Enter id_store: "))
                new_idp = int(input("Enter id_provider: "))
                new_names = str(input("Enter Name: "))
                new_price = int(input("Enter Price: "))
                new_count = int(input("Enter Count: "))
                id_product2.append(item.Item(new_idp, new_ids, new_names, new_price, new_count))
                print("Add item")
                a = {"ID": new_ids, "Name": new_names, "Price": new_price}
                if a not in name_of_product:
                    name_of_product.append(a)
            self.admin_login()
        elif id_provider > 2:
            print("Incorrect number of provider")
            self.admin_login()


    def make_order(self):
        temp = True
        d = []

        while temp:
            if len(name_of_product) == 0:
                print("Oh no, product not be")
            else:
                for index in range(1, len(name_of_product)):
                    for it, amount in name_of_product[index].items():  # dct.iteritems() in Python 2
                        print("{} {}".format(it, amount))
                    print("*******************************")
                p_id = int(input("Enter id: "))
                p_name = str(input("Enter name of product: "))
                p_count = int(input("Enter count: "))
                tmp = True
                index = 1
                while tmp and index != len(name_of_product):
                    if p_name in name_of_product[index].values():
                        d.append(item.Item(p_id, p_id, p_name, 0, p_count))
                        tmp = False
                    index += 1
                if tmp:
                    print("No items")

                print("Do you want to add products? Y/N ")
                conform = input()
                if conform == "Y" or conform == "y":
                    temp = True
                else:
                    temp = False

        print("\n**********************************************\n")
        print("Thank you!")
        s = store.Store()
        s.take_order(d, self.__address)
