class Pile:

    def __init__(self):
        self.__len = 0
        self.__data = []

    def is_empty(self) -> bool:
        return self.__len == 0

    def push(self, e):
        self.__len += 1
        self.__data.append(e)

    def pop(self):
        assert not self.is_empty()
        self.__len -= 1
        res = self.__data[self.__len]
        self.__data = self.__data[:-1]

        return res
