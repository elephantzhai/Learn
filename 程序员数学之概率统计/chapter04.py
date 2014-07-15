import Cdf
import random
import myplot
import Pmf
import erf
import descriptive
import rankit
import relay
import brfss
import thinkstats
import math
import continuous
import populations
import irs
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

# 4-10-1
def NormalPlot(ys):
	n = len(ys)
	xs = [random.normalvariate(0,1) for i in range(n)]
	ys.sort()
	xs.sort()
	myplot.Clf()
	myplot.Plot(xs,ys)
	myplot.show()

def MakeNormalPolt():
	ys = [i for i in range(100)]
	NormalPlot(ys)
# 4-10-2
def RelayNormal():
	results = relay.ReadResults()
	speeds = relay.GetSpeeds(results)
	NormalPlot(speeds)

# 4-11
def Brfss_figs():
	resp = brfss.Respondents()
	resp.ReadRecords()
	print len(resp.records)
	results = [r.wtkg2 for r in resp.records if r.wtkg2 != 'NA']
	cdf = Cdf.MakeCdfFromList(results)
	t = results[:]
	t.sort()
	mean,var = thinkstats.TrimmedMeanVar(t)
	print 'len,mean,var',len(t),mean,var
	sigma = math.sqrt(var)
	myplot.Clf()
	xs,ps = continuous.RenderNormalCdf(mean,sigma,175)
	myplot.Plot(xs,ps)
	xs,ps = cdf.Render()
	myplot.Plot(xs,ps)
	myplot.show()
# 4-12-2
def populations2():
	results = populations.ReadData()
	cdf = Cdf.MakeCdfFromList(results)
	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show()

# 4-12-3
def population3():
	results = populations.ReadData()
	cdf = Cdf.MakeCdfFromList(results)
	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show(xscale = 'log')
	# myplot.show(xscale = 'log',yscale = 'log')

# 4-12-4
def population4():
	results = populations.ReadData()
	# cdf = Cdf.MakeCdfFromList(results)
	t = [math.log(p)for p in results]
	NormalPlot(t)

# 4-13
def Irs():
	data = irs.ReadIncomeFile()
	print 1
	hist, pmf, cdf = irs.MakeIncomeDist(data)
	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show(xscale = 'log')


if __name__  == '__main__':
	# expovariateTest()
	# ParetovariateTest()
	# HeightInWorld()
	# WeibullDistribution()
	# Intelligence();
	# BirthDate()
	# RanKit()
	# MakeNormalPolt()
	# RelayNormal()
	# Brfss_figs()
	# populations2()
	# population3()
	# population4()
	Irs()