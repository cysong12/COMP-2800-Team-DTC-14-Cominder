from Cominder.users.reminder_feature_temp import User
from enum import Enum
import datetime


class Fridge:
    def __init__(self, **kwargs):
        self.__items_dict = {}

        self.add_items(**kwargs)

    def get_items_dict(self):
        return self.__items_dict

    def get_number_of_an_item(self, item_name):
        return self.__items_dict[item_name]

    def add_items(self, **kwargs):
        for key in kwargs.keys():
            try:
                self.__items_dict[key] += kwargs[key]
            except KeyError:
                self.__items_dict[key] = kwargs[key]

    def subtract_items(self, **kwargs):
        for key in kwargs.keys():
            try:
                self.__items_dict[key] -= kwargs[key]
            except KeyError:
                return "Item doesn't exist."
            else:
                if self.__items_dict[key] <= 0:
                    del self.__items_dict[key]

    def delete_items(self, args):
        for item in args:
            try:
                del self.__items_dict[item]
            except KeyError:
                return "Item doesn't exist."


# test
def main():
    user = User('Choi', 'Song', datetime.datetime(1992, 12, 18), True, middle_name="Yong")
    user_fridge = Fridge(bananas=5, apples=3, grapes=1)
    print(user_fridge.get_items_dict())
    user_fridge.add_items(oranges=2, watermelon=10)
    print(user_fridge.get_items_dict())
    user_fridge.subtract_items(watermelon=5, apples=4)
    print(user_fridge.get_items_dict())
    user_fridge.delete_items(('grapes', 'oranges'))
    print(user_fridge.get_items_dict())
    print(user_fridge.get_number_of_an_item("bananas"))


if __name__ == "__main__":
    main()
