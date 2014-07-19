import thinkstats
import Pmf
import matplotlib.pyplot as pyplot

# a = [1,2,3,2]
# b = {1:[1,2,3,4],2:[5,6,7,8],3:[9,10,11,12]}
# print sorted(a)[1:-1]
# print thinkstats.Mean(a)
# print thinkstats.Binom(3,2)
# a = a+[4]
# a.append(5)
# print a

# c = {7:8,1:2,3:4,5:6}
# print c.items()
# print sorted(c.items())
# print zip(*sorted(c.items()))

# hist= Pmf.MakeHistFromList([1,2,2,3,5])
# print hist.Freq(2)
# print hist.Values()
# print hist.Items()
# pyplot.pie([1,2,3])
# pyplot.show()

# vals,freqs


# isSee = False

# res = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
# playTimes = len(res)
# continueNum = 10
# isInState = None
# num = 0
# for k in range(playTimes):
# 	p = res[k]==1
# 	if num == 0:
# 		isInState = p
# 		num =1
# 	else:
# 		if isInState == p:
# 			num+=1
# 		else:
# 			if num == continueNum:
# 				isSee = True
# 				continue
# 			else:
# 				if playTimes-k<continueNum:
# 					continue
# 				else:
# 					isInState = p
# 					num = 1
# if num == continueNum:
# 	isSee = True
# print isSee
print 2**2*2