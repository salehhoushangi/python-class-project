import os
class Item:
    # attribute

    #constructor
    def __init__(self, name, count,cost):
        self.name = name
        self.count = count
        self.cost = cost
    # properties
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = value
        else:
            raise TypeError("value must be int data type.")

    @property
    def cost(self):
        return self.__cost
    
    @cost.setter
    def cost(self, value):
        if isinstance(value, float):
            self.__cost = value
        else:
            raise TypeError("value must be int data type.")

    # method
    # 
    # magic method    
    def __add__(self, other):
        total = self.__count + other
        self.__count = total
        return total
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.__count = self.__count + other
            return self
        else:
            raise TypeError("other must be int data type.")
    
    def total_price(self):
        price = self.__count * self.__cost
        return price


    # casting
    def __str__(self):
        return '{} {}'.format(self.__name, self.__count)
    
    def __int__(self):
        return self.__count
    
    def __float__(self):
        return float(self.__count)

    # representation of an object
    def __repr__(self):
        return '(item name :{}, item count:{}, cost:{}, totalprice:{})'.format(self.__name, self.__count,self.__cost,self.total_price())

class Items:
    def __init__(self):
        self.__items = list()
    
    def add(self, item):
        if isinstance(item, Item):
            if item in items:
                print("your item exist")
            else:
                self.__items.append(item)
        else:
            raise TypeError("value must be Item class.")

    def show(self):
        return self.__items

    def __iter__(self):
        yield from self.__items
    
    def __contains__(self, item):
        for i in self:
            if item.name == i.name and item.count == i.count:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self
    
    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
class user:
    def __init__(self,username):
        self.username = username
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__username = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")
    def show_username(self):
        print("your username is {}".format(self.__username))
    def username_file(self):
        if os.path.exists(self.__username):
            with open(self.__username , "r+") as file :
                print("your username {} is exist".format(self.__username))
                print(file.read())
        else:
            with open(self.__username , "w") as file :
                print(file.write("hello"))


class category:
    
    total_category = ['grocery','electronic','fruit','book']
    def __init__(self,category_name):
        self.category_name = category_name

    @property
    def category_item(self):
        return self.__category_item

    @category_item.setter
    def category_item(self,value):
        if isinstance(value, str):
            if value.isalpha():
                self.__category_item = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")
    def add_category(self,)

items = Items()
user1 = user(input("Enter your username:\n"))
user.show_username(user1)
user.username_file(user1)



while True :

    item = Item(input("enter your item:"),int(input("input your count item:")),float(input("input your cost item:")))
#item2 = Item('orange', 2)
    items.add(item)
    print(items)












