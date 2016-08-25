def tStatistic(xf, xm, se):
    return (xf-xm)/se

assert(tStatistic(33.14, 18, 15.72) == 0.9631043256997456)
assert(tStatistic(33.14, 12, 15.72) != 0.9631043256997456)