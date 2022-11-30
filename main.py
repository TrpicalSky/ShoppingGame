from store import Shop
from item import Item
from shopper import Person

person = Person()
person.addMoney(2.50)
storeVar = Shop()
apple = Item("Apple", 0)
taco = Item("Apple", 2900)
pie = Item("Apple", 0)
potatoe = Item("Apple", 0)

print(person.addItem(storeVar,items=[apple,taco,pie]))