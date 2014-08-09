import thinkstats
import math
import brfss
# 9-1
def Cov(l1,l2):
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
	print Cov(l1,l2)

# 9-2
def Corr(l1,l2):
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
	print Corr(l1,l2)

# 9-3
def MapToRanks(t):

	pairs = enumerate(t)

	sorted_pairs = sorted(pairs,key = lambda pair:pair[1])

	trips = enumerate(sorted_pairs)

	resorted = sorted(trips,key = lambda trip:trip[1][0])

	ranks = [trip[0]+1 for trip in resorted]

	return ranks

def SpearmanRank(l1,l2):
	r1 = MapToRanks(l1)
	r2 = MapToRanks(l2)

	return Corr(r1,r2)

def SpearmanRankTest():
	l1 = [1,2,3,4,5]
	l2 = [2,3,4,5,6]
	print SpearmanRank(l1,l2)

# 9-4
class Respondents(brfss.Respondents):

	def GetHeightAndWeight(self):
		heights = []
		weights = []
		for r in self.records:
			if r.wtkg2 == 'NA' or r.htm3 == 'NA':
				continue
			heights.append(r.htm3)
			weights.append(r.wtkg2)
		return heights,weights
def LogList(l):
	r = []
	for i in l:
		r.append(math.log(i))
	return r

def BrfssTest():
	resp = Respondents()
	resp.ReadRecords()

	heights,weights = resp.GetHeightAndWeight()
	print 'num: ',len(heights)
	print Corr(heights,weights)

	logWeights = LogList(weights)
	print Corr(heights,logWeights)
	print SpearmanRank(heights,logWeights)

if __name__ == "__main__":
	# CovTest()
	# CorrTest()
	# SpearmanRankTest()
	BrfssTest()