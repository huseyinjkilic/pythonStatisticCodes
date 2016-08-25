def calculateDeggreeOfFreedom(sample1, sample2):
    return sample1 + sample2 - 2

assert(calculateDeggreeOfFreedom(7 ,11) == 16)
assert(calculateDeggreeOfFreedom(7 ,12) != 16)