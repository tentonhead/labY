from si_units.si import units, exponent


class SampleMeta:
    def __init__(self, column_title):
        self.units    = units(column_title)
        self.exponent = exponent(column_title)
