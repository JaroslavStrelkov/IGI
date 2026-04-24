import abc

class Figure(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass