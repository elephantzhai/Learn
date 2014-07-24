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


def ReSample(model1,model2,n,m):
	t1 = SampleWithReplayment(model1,n)
	t2 = SampleWithReplayment(model2,m)
	delta = thinkstats.Mean(t1) - thinkstats.Mean(t2)
	return delta

def PValue(model1,model2,n,m,delta,iter = 1000):

	deltas = [ReSample(model1,model2,n,m) for i in range(iter)]

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





if __name__ == '__main__':
	AverageDiffTest()
