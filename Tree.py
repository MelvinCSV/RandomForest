class Tree:

    def __init__(self, is_leaf: bool, data=None, value=None):
        self.__is_leaf = is_leaf
        self.__data = data
        self.__value = value
        self.__children = []

    def get_data(self):
        return self.__data

    def get_value(self):
        assert self.__is_leaf
        return self.__value

    def get_children(self):
        return self.__children

    def set_data(self, data):
        self.__data = data

    def set_value(self, value):
        assert self.__is_leaf
        self.__value = value

    def add_children(self, children):
        assert isinstance(children, Tree)
        self.__children.append(children)

    def is_leaf(self) -> bool:
        return self.is_leaf()


if __name__ == '__main__':
    my_tree = Tree(False)
    print(1)
