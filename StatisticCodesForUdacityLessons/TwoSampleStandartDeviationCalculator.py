from math import sqrt
from math import pow

def standartError(sf, nf, sm, nm):
    return sqrt((pow(sf,2)/nf) + (pow(sm,2)/nm))

#Unit Test about function
assert(standartError(31.36, 7, 34.27, 11) == 15.724484960491624)
assert(standartError(31.33, 7, 34.27, 11) != 15.724484960491624)