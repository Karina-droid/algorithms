#X = Xl*2^(n/2) + Xr
#Y = Yl*2^(n/2) + Yr
#XY = (Xl*2^(n/2) + Xr)(Yl*2^(n/2) + Yr) = 2^n*XlYl + 2^(n/2)*(XlYr + XrYl) + XrYr
#XlYr + XrYl = (Xl + Xr)(Yl + Yr) - XlYl- XrYr
#XY = 2^n * XlYl + 2^(n/2) * [(Xl + Xr)(Yl + Yr) - XlYl - XrYr] + XrYr

#the recurrence - T(n) = 3T(n/2) + O(n), the solution - O(n^1.59)

def make_equal_length(str1, str2):
    """ given 2 strings of unequal length, adds leading 0s to the smaller one
        returns the new length """
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        for i in range(len2 - len1):
            str1 = '0' + str1
        return len2
    elif len1 > len2:
        for i in range(len1 - len2):
            str2 = '0' + str2
    return len1


def add_bit_strings(first, second):
    """adds two bit sequences and returns the addition"""
    
