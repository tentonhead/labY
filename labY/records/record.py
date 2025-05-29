import numpy as np

class Record:
    def __init__(self, data: np.ndarray, label: str):
        self.data = np.array(data)
        self.label = label

    def round(self, precision):
        return Record(np.round(self.data, precision), self.label)

    def floor(self):
        return Record(np.floor(self.data), self.label)

    def ceil(self):
        return Record(np.ceil(self.data), self.label)

    """Arithmetic operations are equivalent to calling data field and performing
    operations on them. Defined through magic methods for convinience.
    """
    def _operate(self, other, operation_func):
        """Template for arithmetic functions."""
        if isinstance(other, Record):
            result_data = operation_func(self.data, other.data)
            return Record(result_data, self.label)
        elif isinstance(other, (int, float, np.number)):
            result_data = operation_func(self.data, other)
            return Record(result_data, self.label)
        else:
            e = "Operand must be a Record instance or a numeric type"
            raise ValueError(e)

    def __add__(self, other):
        return self._operate(other, np.add)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self._operate(other, np.subtract)

    def __rsub__(self, other):
        return self._operate(other, lambda x, y: y - x)

    def __mul__(self, other):
        return self._operate(other, np.multiply)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self._operate(other, np.divide)

    def __rtruediv__(self, other):
        return self._operate(other, lambda x, y: y / x)

    def __floordiv__(self, other):
        return self._operate(other, np.floor_divide)

    def __rfloordiv__(self, other):
        return self._operate(other, lambda x, y: y // x)

    def __mod__(self, other):
        return self._operate(other, np.mod)

    def __rmod__(self, other):
        return self._operate(other, lambda x, y: y % x)

    def __pow__(self, other):
        return self._operate(other, np.power)

    def __rpow__(self, other):
        return self._operate(other, lambda x, y: y ** x)

    def __repr__(self):
        return f"Record:{self.label} = {self.data}"

def N(number: int):
    return Record(np.array([i for i in range(1, number+1)]), "N")
