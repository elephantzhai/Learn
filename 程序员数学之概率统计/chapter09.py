import thinkstats
import math
# 9-1
def Cov(pairs):
	l1,l2 = zip(*pairs)

	mean1 = thinkstats.Mean(l1)
	sigma1 = math.sqrt(thinkstats.Var(l1))
	mean2 = thinkstats.Mean(l2)
	sigma2 = math.sqrt(thinkstats.Var(l2))

	X,Y = [],[]
	for i in l1:
		X.append((i - mean1)/sigma1)
	for i in l2:
		Y.append((i - mean2)/sigma2)

	n = len(X)
	cov = 0
	for i in range(n):
		cov += X[i]*Y[i]
	cov /= n

	return cov

def CovTest():
	l1 = [1,2,3,4,5,6]
	l2 = [1,3,5,7,9,11]
	pairs = zip(l1,l2)
	print Cov(pairs)

# 9-2
def Corr(pairs):
	l1,l2 = zip(*pairs)

	mean1 = thinkstats.Mean(l1)
	sigma1 = math.sqrt(thinkstats.Var(l1))
	mean2 = thinkstats.Mean(l2)
	sigma2 = math.sqrt(thinkstats.Var(l2))

	X,Y = [],[]
	for i in l1:
		X.append((i - mean1)/sigma1)
	for i in l2:
		Y.append((i - mean2)/sigma2)

	n = len(X)
	cov = 0
	for i in range(n):
		cov += X[i]*Y[i]
	cov /= n

	sigmaX = math.sqrt(thinkstats.Var(X))
	sigmaY = math.sqrt(thinkstats.Var(Y))

	return cov/(sigmaX*sigmaY)

def CorrTest():
	l1 = [1,2,3,4,5,6]
	l2 = [1,3,5,7,9,11]
	pairs = zip(l1,l2)
	print Corr(pairs)


if __name__ == "__main__":
	# CovTest()
	CorrTest()