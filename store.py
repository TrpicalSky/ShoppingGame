from item import Item


class Shop:
    def __init__(self) -> None:
        self.items = list[Item]()

    def addItemToStore(self,item:Item) -> list[Item]:
        self.items.append(item)
        return self.items

    def removeItemFromStore(self,item:Item) -> list[Item]:
        if (item in self.items):
            self.items.remove(item)
        else:
            print(f"There is no item in the list with the name {item.name}")
        return self.items

    