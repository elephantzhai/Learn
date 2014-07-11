import Cdf
import random
import myplot
import Pmf
import erf
import descriptive
# 4-1
def expovariateTest():
	results = []
	lamada = 1.0/32.6
	for i in range(44):
		results.append(random.expovariate(lamada))

	cdf = Cdf.MakeCdfFromList(results)
	myplot.Clf()
	myplot.Cdf(cdf,complement=True,xscale = 'linear',yscale = 'log')
	myplot.show()

# 4-3
def ParetovariateTest():
	results = []
	a=1
	xm=0.5
	for i in range(1000):
		results.append(random.paretovariate(a)*xm)
	cdf = Cdf.MakeCdfFromList(results)
	myplot.Clf()
	myplot.Cdf(cdf,complement=True,xscale = 'log',yscale = 'log')
	myplot.show()
# 4-4
def HeightInWorld():
	results = []
	a = 1.7
	xm = 100
	sampleNum = 6000
	for i in range(sampleNum):
		results.append(random.paretovariate(a)*xm)
	cdf = Cdf.MakeCdfFromList(results)
	average = cdf.Mean();
	print 'average',average

	lowNum = 0
	for height in results:
		if height < average:
			lowNum += 1
	print 'low percent',lowNum*1.0/sampleNum

	heighest = 0
	for height in results:
		if heighest<height:
			heighest = height
	print 'heighest',heighest
# 4-6
def WeibullDistribution():
	results = []
	k = 2
	lamada = 1

	sampleNum = 6000
	for i in range(sampleNum):
		results.append(random.weibullvariate(lamada,k))
	cdf = Cdf.MakeCdfFromList(results)
	myplot.Clf()
	myplot.Cdf(cdf,complement=True,xscale = 'log',yscale = 'log')
	# myplot.Cdf(cdf)
	myplot.show()
# 4-7
def Intelligence():
	print '>115',1-erf.NormalCdf(115,mu = 100,sigma = 15)
	print '>130',1-erf.NormalCdf(130,mu = 100,sigma = 15)
	print '>145',1-erf.NormalCdf(145,mu = 100,sigma = 15)
	print '>190 people',(1-erf.NormalCdf(190,mu = 100,sigma = 15))*60*100000000
# 4-8
def BirthDate():
	pool,first,other = descriptive.MakeTables()
	pmf = pool.pmf
	print 'mean',pmf.Mean()
	print 'var',pmf.Var()

	cdf = Cdf.MakeCdfFromPmf(pmf)
	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show()
# 4-9
def Sample():
	results = []
	for i in range(6):
		results.append(random.normalvariate(0,1))
	results.sort()
	return results

def Samples():
	results1 = []
	for i in range(1000):
		results1.append(Sample())
	results2 = zip(*results1)
	results3 = []
	for tempList in results2:
		results3.append(sum(tempList)/len(tempList))
	print results3


def RanKit():
	Samples()

if __name__  == '__main__':
	# expovariateTest()
	# ParetovariateTest()
	# HeightInWorld()
	# WeibullDistribution()
	# Intelligence();
	# BirthDate()
	RanKit()