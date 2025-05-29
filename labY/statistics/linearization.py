import numpy as np

from .stats import standard_deviation, sigma
from ..records.record import Record, N
from ..table.table import Table


class LeastSquares():
    """The same table as before but methods are tweaked to write less code in 
    scripts.
    """
    def __init__(self, record1:Record, record2: Record, presicion=3):
        """Creates names and contents from given arguments. Calculates contents
        averages and deviations with coefficients.
        """
        self.a_coef = 0
        self.b_coef = 0
        self.averages = []
        self.deviations = []
        self.records = []
        
        def set_names(col1_name, col2_name):
            """
            Creates names for 2, 4 and 5th columns based on provided names.
            col2_name is actually third column.
            """
            names = ["" for i in range(6)]
            names[0] = "N"
            names[1] = col1_name
            names[3] = col2_name

            def x_squared_name(name, i):
                if ',' in name:
                    names[i] = (name.split(',')[0]+"^2," +
                            name.split(',')[1]+"^2")
                else:
                    names[i] = name+"^2"

            x_squared_name(col1_name, 2)
            x_squared_name(col2_name, 4)
            names[5] = (col1_name.split(',')[0] + "*" +
                        col2_name.split(',')[0])
            if col1_name.count(',') == col2_name.count(',') == 1:
                names[5] += (" " +col1_name.split(',')[1] + "*" +
                             col2_name.split(',')[1])
            return names

        def calc_contents(x, y):
            """Implements all logic in least squares method."""
            n = len(x)
            N = np.arange(1, n+1)
            x2 = np.round(np.copy(x)**2, presicion)
            y2 = np.round(np.copy(y)**2, presicion)
            xy = np.round(x*y, presicion)
            contents = [N, x, x2, y, y2, xy]

            def avg(data):
                return round(sum(data)/n, presicion)

            #print(presicion)
            σx = avg(x2) - avg(x)**2
            σy = avg(y2) - avg(y)**2
            σx = round(σx, presicion)
            σy = round(σy, presicion)

            a = (avg(xy) - (avg(x)*avg(y))) / σx
            b = avg(y) - a*avg(x)
            self.a_coef = a; self.b_coef = b

            σa = np.sqrt((1/(n-2))*((σy/σx) - a**2))
            σb = σa*np.sqrt(avg(x2))
            σa = round(σa, presicion)
            σb = round(σb, presicion)
            self.averages = [avg(x), avg(x2), avg(y), avg(y2), avg(xy)]
            self.deviations = [σx, σy, σa, σb]
            return contents

        names = set_names(record1.label, record2.label)
        contents = calc_contents(record1.data, record2.data)
        for i in range(len(names)):
            self.records.append(Record(contents[i], names[i]))

        #super().__init__(records)
        print("Created a \"least squares\" table")

    def coefficients(self):
        """Returns a - slope and b - offset coefficients of line."""
        return self.a_coef, self.b_coef

    def table(self):
        return Table(*self.records)

    def outro(self):
        outro_string = (self.coefficients_string()
                        + self.averages_string()
                        + self.deviations_string()
                        )
        return outro_string


    def coefficients_string(self):
        string = f"A = {self.a_coef}, B = {self.b_coef}\n"
        return string

    def averages_string(self):
        avg = self.averages
        x = self.records[1].label; y = self.records[3].label
        string = (f"\t<{x}>={avg[0]}; <{x}^2>={avg[1]};\n"
                  + f"\t<{y}>={avg[2]}; <{y}^2>={avg[3]}; <{x}*{y}>={avg[4]}\n")
        return string

    def deviations_string(self):
        x = self.records[1].label.split(',')[0]
        y = self.records[3].label.split(',')[0]
        #self.deviations = [σx, σy, σa, σb]
        dev = self.deviations
        string = (f"\tσ^2_{x}={dev[0]}, σ^2_{y}={dev[1]}\n"
                  + f"\tσa={dev[2]}, σb={dev[3]}\n")
        return string

"""
def least_squares(x, y, names, presicion=3):
    #Uses least squares to calculat a and b coefficients of line
    #Returns a, b, collumns of squares [x, x^2, y, y^2, x*y],
    #list of their averages in respecting order, and list of deviations
    #[x, y, a, b]. SHOUD PROBABLY RETURN THEM AS STRINGS and add 2 separate 
    #presicions
    n = len(x)
    N = np.arange(1, n+1)
    x2 = np.round(np.copy(x)**2, presicion)
    y2 = np.round(np.copy(y)**2, presicion)
    xy = np.round(x*y, presicion)
    contents = [N, x, x2, y, y2, xy]
    def avg(data):
        return round(sum(data)/n, presicion)
    σx = avg(x2) - avg(x)**2
    σy = avg(y2) - avg(y)**2
    #print(avg(xy), avg(x)*avg(y), σx)
    a = (avg(xy) - (avg(x)*avg(y))) / σx
    b = avg(y) - a*avg(x)
    σa = math.sqrt((1/(n-2))*((σy/σx) - a**2))
    σb = σa*math.sqrt(avg(x2))
    averages = [avg(x), avg(x2), avg(y), avg(y2), avg(xy)]
    deviations = [σx, σy, σa, σb]
    print(f"a = {a}; b = {b}")
    print(f"Avg: x={averages[0]}; x^2={averages[1]};")
    print(f"y={averages[2]}; y^2={averages[3]}; <xy>={averages[4]}")
    print(f"dev: σx={σx}, σy={σy}, σa={σa}, σb={σb}")
    #table = Table(names, contents)
    return a, b, contents, averages, deviations
"""

class PairPoint(): #SHOULD RETURN TABLE
    """Calculates angle using method of pairs of points
    and it's standard deviation
    """
    def __init__(self, x: Record, y: Record, letter="", units="", multiplier=1):
        #def __init__(self, x: Record, y: Record, headings, unit):
        if len(x.data)%2 != 0:
            print("Number of points must be even in order to use PPM")
            return 0, 0, 0
        pairs = len(x.data)//2
        x1 = x.data[0:pairs]; x2 = x.data[pairs:]
        y1 = y.data[0:pairs]; y2 = y.data[pairs:]
        self.x, self.y = x, y
        self.n = N(pairs)
        self.angles = Record((x2-x1) / (y2-y1)*multiplier, f"{letter}, {units}")
        self.angle = np.average(self.angles.data)
        self.sigma = 0.0
        self.avg_dif, self.avg_dif2 = standard_deviation(self.angles, letter)
        self.sigma = sigma(self.avg_dif2)

    """
    def angle(self):
        return self.angle
    """
    def points(self):
        gap = self.n//2
        s = ["" for i in range(gap)]
        for i in range(1, len(s)+1):
            # Wait, can I print column of strings?
             s[i] = f"{i+gap}-{i}"
             
    def table(self):
        return Table(self.n, self.x, self.y, self.angles,
                     self.avg_dif, self.avg_dif2)
