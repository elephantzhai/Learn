import Cdf
import random
import myplot
import Pmf
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



if __name__  == '__main__':
	# expovariateTest()
	# ParetovariateTest()
	HeightInWorld()