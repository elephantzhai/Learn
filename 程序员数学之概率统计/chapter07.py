import random
import readsurvey
import thinkstats
import Cdf
import myplot

# 7-1
def MeanAndDiff(l1,l2):
	m1 = thinkstats.Mean(l1)
	m2 = thinkstats.Mean(l2)
	delta = m1-m2
	return m1,m2,delta

def SampleWithReplayment(model,n):
	return [random.choice(model) for i in range(n)]

def SamleWithoutRelayment(model,n):
	return random.sample(model,n)

def ReSample(model1,model2,n,m,isRelay = True):
	if isRelay:
		t1 = SampleWithReplayment(model1,n)
		t2 = SampleWithReplayment(model2,m)
	else:
		t1 = SamleWithoutRelayment(model1,n)
		t2 = SamleWithoutRelayment(model2,m)

	delta = thinkstats.Mean(t1) - thinkstats.Mean(t2)
	return delta

def PValue(model1,model2,n,m,delta,isRelay = True,iter = 1000):

	deltas = [ReSample(model1,model2,n,m,isRelay) for i in range(iter)]

	cdf = Cdf.MakeCdfFromList(deltas)

	left = cdf.Prob(-delta)
	right = 1.0- cdf.Prob(delta)

	pvalue = left+right

	return cdf,pvalue


def AverageDiffTest():
	random.seed(1)

	pool,first,others = readsurvey.MakeTables()

	n = len(first.weights)
	m = len(others.weights)
	firstMean,othersMean,delta = MeanAndDiff(first.weights,others.weights)
	delta = abs(delta)

	cdf,pvalue = PValue(pool.weights,pool.weights,n,m,delta)

	print delta,pvalue

	myplot.clf()
	myplot.Cdf(cdf)
	myplot.show()

# 7-2
def Partition(list1,n):
	random.shuffle(list1)
	return list1[n:],list1[:n]

def Test(actual1,actual2,model1,model2,isRelay = True):
	n = len(actual1)
	m = len(actual2)

	firstMean,othersMean,delta = MeanAndDiff(actual1,actual2)
	delta = abs(delta)
	cdf,pvalue = PValue(model1,model2,n,m,delta,isRelay)

	return cdf,pvalue

def PartitionDiffTest():
	random.seed(1)
	pool,first,others = readsurvey.MakeTables()

	partitionRate = 1.0*1/2
	partitionSize = int(len(pool.lengths)*partitionRate)
	n = int(len(first.lengths)*partitionRate)
	m = int(len(others.lengths)*partitionRate)
	actual1,model1 = Partition(first.lengths,n)
	actual2,model2 = Partition(others.lengths,m)
	modelPool = model1+model2

	# firstMean,othersMean,delta = MeanAndDiff(actual1,actual2)
	# delta = abs(delta)
	# print len(modelPool),n,m,partitionSize
	# cdf,pvalue = PValue(modelPool,modelPool,n,m,delta,isRelay = False)
	cdf,pvalue = Test(actual1,actual2,modelPool,modelPool,isRelay = False)
	print pvalue

	myplot.clf()
	myplot.Cdf(cdf)
	myplot.show()

#7-3
def PosteriorProbability():
	pool,first,others = readsurvey.MakeTables()

	# n = len(first.weights)
	# m = len(others.weights)
	# firstMean,othersMean,delta = MeanAndDiff(first.weights,others.weights)
	# delta = abs(delta)
	# cdf,pvalue = PValue(first.weights,others.weights,n,m,delta)

	cdf0,peh0 = Test(first.weights,others.weights,pool.weights,pool.weights)
	cdfa,peha = Test(first.weights,others.weights,first.weights,others.weights)

	ph0,pha = 0.5,0.5
	pe = ph0*peh0+pha*peha

	ph0e = peh0*ph0/pe
	phae = peha*pha/pe

	print ph0e,phae




if __name__ == '__main__':
	# AverageDiffTest()
	# PartitionDiffTest()
	PosteriorProbability()
