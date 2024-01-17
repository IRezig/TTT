# private name mangling


class Inventory:
    def __init__(self):
        self.__items = []

    def add_new_item(self, item):
        if type(item) == str:
            self.__items.append(item)
            print("New item added")
        else:
            print("Invalid item")

    def get_number_of_items(self):
        return len(self.__items)


inventory = Inventory()
inventory.add_new_item("item1")
inventory.add_new_item(2)
inventory.add_new_item("item2")
print(inventory.get_number_of_items())
# print(inventory.__items)
# print(inventory._Inventory__items)


# how to use getattr and setattr
# my_items = getattr(inventory, "_Inventory__items")
# print(my_items)
# setattr(inventory, "_Inventory__items", [])
# print(inventory.get_number_of_items())


# Rules for name mangling
# 1. If a name starts with two underscores, and ends with two or more underscores, Python will not perform name mangling.
# Examples:
# self.__my_private_method__  NOT mangled.
# __local  mangled local variable, becomes _ClassName__local
