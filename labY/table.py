import numpy as np

import SI


# Hashing problem
class SampleMeta:
    def __init__(self, title):
        self.units    = SI.units(title)
        self.exponent = SI.exponent(title)


class Measurement:
    def __init__(self, data: np.ndarray, meta: SampleMeta):
        self.data = data
        self.meta = meta


class TableMonster:
    def __init__(self, results: dict[SampleMeta, np.ndarray]):
        self.results = results
