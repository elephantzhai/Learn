﻿import thinkstats
a = [1,2,3,2]
b = {1:[1,2,3,4],2:[5,6,7,8],3:[9,10,11,12]}
print sorted(a)[1:-1]
print thinkstats.Mean(a)
print b[3,1]
print thinkstats.Binom(3,1,b)