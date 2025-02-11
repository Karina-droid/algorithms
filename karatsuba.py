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
    result = ""
    length = make_equal_length(first, second)
    carry = 0

    #add all bits one by one
    for i in range(length-1, -1, -1):
        first_bit = first[i]
        second_bit = second[i]
        sum = (first_bit ^ second_bit ^ carry) + ord('0')
        result = chr(sum) + result
        carry = (first_bit & second_bit) | (first_bit & carry) | (second_bit & carry)

    #if overflow, then add the leading 1
    if carry:
        result = '1' + result

    return result


def multiply_single_bit(a, b):
    return int(a[0])*int(b[0])


def multiply(X, Y):
    """multiplies two bit strings and returns the result as long integer"""
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)

    #base cases
    if n == 0: return 0
    if n == 1: return int(X[0])*int(Y[0])

    fh = n//2   #first half of the string
    sh = n - fh     #second half of the string
    Xl = X[:fh]
    Xr = X[fh:]
    Yl = Y[:fh]
    Yr = Y[fh:]

    #recursively calculate the 3 products of inputs of size n/2
    P1 = multiply(Xl, Yl)
    P2 = multiply(Xr, Yr)
    P3 = multiply(str(int(Xl, 2) + int(Xr, 2)), str(int(Yl, 2) + int(Yr, 2)))

    #combine the 3 products to get the final result
    return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2
