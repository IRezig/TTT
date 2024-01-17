# name mangling protected


class Inventory:
    def __init__(self):
        # don't touch this please
        self._dont_touch_me = "protected"  # protected

    def get_number_of_char(self):
        return len(self._dont_touch_me)

    @property
    def val(self, value):
        self._items = value


inventory = Inventory()
print(inventory.get_number_of_char())
print(inventory._dont_touch_me)
inventory._dont_touch_me = "hello"
print(inventory._dont_touch_me)
