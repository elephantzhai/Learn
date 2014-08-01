import random
import thinkstats

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

if __name__ == '__main__':
	MSETest()