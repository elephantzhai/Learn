import random
import thinkstats
import math

#8-1
def MSE(isAverage = True):
	mu,sigma = 0,1
	mse = 0
	testTime = 1000
	for i in range(testTime):
		test = [random.normalvariate(mu,sigma) for j in range(6)]
		if isAverage:
			difference = thinkstats.Mean(test)
		else:
			test.sort()
			difference = (test[2]+test[3])/2
		mse += (difference)**2
	mse /= testTime
	return mse
def MSETest():
	print MSE()
	print MSE(isAverage = False)

# 8-2
def Estimator(isN = True):
	mu,sigma = 0,1
	testTime = 1000
	s = 0
	itemsNum = 6
	for i in range(testTime):
		test = [random.normalvariate(mu,sigma) for j in range(itemsNum)]
		ss = 0
		aver = thinkstats.Mean(test)
		for tmp in test:
			ss += (tmp-aver)**2
		if isN:
			s += ss/itemsNum
		else:
			s += ss/(itemsNum-1)
	return 1.0*s/testTime - sigma


def EstimatorTest():
	print Estimator(isN = True)
	print Estimator(isN = False)

# 8-3
def Exponential(isAverage = True):
	lamada = 2
	testTime = 1000
	itemsNum = 6
	log2 = math.log(2)
	s = 0
	for i in range(testTime):
		test = [random.expovariate(lamada) for j in range(itemsNum)]
		if isAverage:
			tlamada = 0
			for x in test:
				tlamada += 1.0/x
			tlamada /= itemsNum
		else:
			test.sort()
			middleNum = (test[2]+test[3])/2
			tlamada = log2/middleNum

		s += 1.0/(tlamada**2)

	return s*1.0/testTime

def ExponentialDistributionTest():
	print Exponential(isAverage = True)
	print Exponential(isAverage = False)
	

if __name__ == '__main__':
	# MSETest()
	# EstimatorTest()
	ExponentialDistributionTest()