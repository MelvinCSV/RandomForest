class Tree:

    def __init__(self, is_leaf: bool, data=None):
        self.__is_leaf = is_leaf
        self.__data = data
        self.__children = []

    def get_data(self):
        assert self.__is_leaf
        return self.__data

    def get_children(self):
        return self.__children

    def set_data(self, data):
        self.__data = data
