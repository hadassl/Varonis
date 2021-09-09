# Use collections in order to demonstrate userlist - Super class for MagicList
from collections import UserList


class MagicList(UserList):

    def __init__(self, cls_type=None):
        super(MagicList, self).__init__()
        self.cls_type = cls_type

    def __set_item__(self, place, value):
        """
        This fuction set an item in the list based on place and value parameters
        :param place: int number
        :param value: int value
        """
        # check for indexErrors
        if len(self.data) == place or place < 0:
            self.data.append(value)
        else:
            super().__setitem__(place, value)

    def __get_item__(self, place):
        """
        This function get a place and return the list item in this specific place
        :param place: int number
        :return: list item
        """
        # check for indexErrors
        if len(self.data) == place or place < 1:
            self.data.append(self.cls_type())
        return super().__getitem__(place)