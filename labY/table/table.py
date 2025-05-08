import math
import sys

import numpy as np

from ..records.record import Record


class Table():
    """Represents a table of measurements we write on paper.
    Names and contents are both lists. By indexing them you can access a
    particular column. Names include heading for each column while contents
    include all data in that column converted to numpy NDArray.
    """
    def __init__(self, *records):
        """Initializes all attributes and sets them to uasble values."""
        self.records = records
        self.columns  = len(records)
        self.rows     = len(records[0].data)

        self.leading_characters_max      = [0 for i in range(self.columns)]
        self.fractional_characters_max   = [0 for i in range(self.columns)]
        self.nzfractional_characters_max = [0 for i in range(self.columns)]


        def compute_column_width(self):
            """Sets limits for how many symbols can be present from either side
            of dot if it is present. In the absense of dot, only
            leading_characters_max attibute is used to center cells.
            """
            for i in range(self.columns):
                max_leading = 0; max_fractional = 0; max_nzfractional = 0;

                for j in range(len(self.records[i].data)):
                    entry = str(self.records[i].data[j]).split(".")
                    leading = len(entry[0])
                    max_leading = max(leading, max_leading)
                    # if leading > max_leading:
                    if len(entry) > 1:
                        fract    = len(entry[1])
                        nz_fract = fract - entry[1].count("0")
                        max_fractional   = max(fract, max_fractional)
                        max_nzfractional = max(nz_fract, max_nzfractional)

                self.leading_characters_max[i]      = max_leading
                self.fractional_characters_max[i]   = max_fractional
                self.nzfractional_characters_max[i] = max_nzfractional

        compute_column_width(self)

    def print(self, file=sys.stdout):
        """Writes a neat formatted table into file object
        and leaves it open (stdout by default)
        """
        def center(self, indx):
            """Figures out how many spaces are needed to allign name from left 
            and right and returns them as 2 integers
            """
            name_len = len(self.records[indx].label)
            max_len  = self.leading_characters_max[indx]
            if self.fractional_characters_max[indx] > 0:
                max_len += 1 + self.fractional_characters_max[indx] 

            diff = max_len - name_len
            if diff < 0:
                l = 1 
                r = 1
            else:
                l = int(diff/2) + 1
                r = int(diff/2) + 1
                if diff%2 != 0:
                    l += 1
            return l, r

        heading = ""
        for i in range(self.columns):
            l, r = center(self, i)
            heading += "|" +l*" " + self.records[i].label + r*" "
        heading += "|\n"
        file.write(heading)

        def allign_coefficients(self, string, col_indx):
            """Figures out how many spaces are needed to allign number cell
            from left and right and returns them as 2 integer coefficients.
            """
            cell = string.split(".")
            left =  self.leading_characters_max[col_indx] - len(cell[0])

            if len(cell) > 1:
                right = self.fractional_characters_max[col_indx] - len(cell[1])
            else:
                right = 0

            diff = len(self.records[col_indx].label) - (len(string)+left+right)
            if diff > 0:
                left  += int(diff/2)
                right += int(diff/2)
                if diff%2 != 0:
                    left += 1
            return left + 1, right + 1
        
        def top_border(self):
            """Returns "+-" string that can be used to separate each row."""
            line = ""
            for i in range(self.columns):
                s = self.leading_characters_max[i] + 2
                if self.fractional_characters_max[i] > 0:
                    s += self.fractional_characters_max[i] + 1

                name_len = len(self.records[i].label)
                if s <= name_len:
                    s += name_len - s + 2

                line += "+"+"-"*s
            line+="+\n"
            return line

        separator = (top_border(self))
        file.write(separator)

        for r in range(self.rows):
            row = ""
            for c in range(self.columns):
                cell = str(self.records[c].data[r])
                left, right = allign_coefficients(self, cell, c)
                row += "|" + left*" " + cell + right*" "
            row += "|\n"
            file.write(row)
            #file.write(separator)
        print("Check the file")



