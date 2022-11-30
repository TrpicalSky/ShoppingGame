from item import Item
from store import Shop

class Person:
    def __init__(self) -> None:
        self.items = list[Item]()
        self.money:float = 0

    def addItem(self, store:Shop ,item:Item =None, items:list[Item]= None) -> list[Item]:
        if item != None:
            if (item in store.items):
                if (self.money >= item.price):
                    self.items.append(item)
                    self.money -= item.price
                    return self.items
                else:
                    return print("You do not have enough money to add this item to the cart!")
            else:
                print(f"The {item.name} that you want is not in your store.")
        else:
            for x in items:
                if (x in store.items):
                    if (self.money >= x.price):
                        self.items.append(x)
                        self.money -= x.price
                    else:
                        print(f"The item you cannot add to your cart is {x.name}.")
                else:
                    print(f"The {x.name} that you want is not in your store.")
            return self.items


    def addMoney(self,money:float) -> float:
        self.money += money
        return self.money

    def removeItemsFromCart(self, item:Item =None, items:list[Item]=None) -> list[Item]:
        if item != None:
            self.items.remove(item)
            self.addMoney(item.price)
            return self.items
        else:
            for x in items:
                self.items.remove(x)
                self.addMoney(x.price)
            return self.items