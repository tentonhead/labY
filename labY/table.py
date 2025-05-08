import numpy as np

import SI


# Hashing problem

class Measurement:
    def __init__(self, data: np.ndarray, title):
        self.data        = data
        self.units       = SI.units(title)
        self.exponent    = SI.exponent(title)
        self.type_direct = False


class TableMonster:
    def __init__(self, results: dict[SampleMeta, np.ndarray]):
        self.results = results
