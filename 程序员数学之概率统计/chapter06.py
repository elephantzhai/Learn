
import survey
import thinkstats
import math
import irs
import Pmf
import random
import brfss
import erf
import myplot
import Cdf
# 6-1-1
def Skewness(samples):
	l = len(samples)
	u = sum(samples)*1.0/l
	tmp1,tmp2 = 0,0

	for i in range(l):
		tmp1 += (samples[i]-u)**2
		tmp2 += (samples[i]-u)**3
	m2,m3 = tmp1/l,tmp2/l
	g1 = m3/((m2**3)**0.5)
	return g1


# 6-1-2	
def Skewness2():
	table = survey.Pregnancies()
	table.ReadRecords()
	pregLengths = [record.prglength for record in table.records]
	print Skewness(pregLengths)

# 6-1-3
def PearsonSkewness():
	table = survey.Pregnancies()
	table.ReadRecords()
	pregLengths = [record.prglength for record in table.records]
	mean,var = thinkstats.MeanVar(pregLengths)
	sigma = math.sqrt(var)
	pregLengths.sort()
	mid = pregLengths[len(pregLengths)/2]
	print mean,var,mid
	print 3*(mean-mid)/sigma
	

def SkewnessTest():
	# samples = [2,2,3,4,5,6]
	# print Skewness(samples)
	Skewness2()
	# PearsonSkewness()

# 6-3
def SkewnessPmf(pmf,mean):
	m2,m3 = 0,0
	for value,p in pmf.Items():
		m2 += p*(value-mean)**2
		m3 += p*(value-mean)**3
	g1 = m3/m2**(3/2)
	return g1

def Gini():
	data = irs.ReadIncomeFile()
	hist, pmf, cdf = irs.MakeIncomeDist(data)

	mean = pmf.Mean()
	var = pmf.Var()
	items =  hist.Items()
	items.sort()
	total = hist.Total()
	middleNum = total/2
	middle = 0
	for salary,num in items:
		if num>=middleNum:
			middle = salary
			break
		else:
			middleNum -= num

	g1 = SkewnessPmf(pmf,mean)

	gp = 3*(mean-middle)/math.sqrt(var)

	diff = Pmf.Pmf()
	for v1,p1 in pmf.Items():
		for v2,p2 in pmf.Items():
			diff.Incr(abs(v1-v2),p1*p2)

	gini = diff.Mean() / mean /2

	print 'mean',mean
	print 'middle',middle
	print 'g1',g1
	print 'gp',gp
	print 'gini',gini

# 6-4
class GumbelDistribution():
	def __init__(self,u,beta):
		self.u = u
		self.beta = beta

	def generate(self):
		x = random.random()
		tmp1 = (x-self.u)/self.beta*-1
		tmp2 = math.exp(tmp1)*-1
		return math.exp(tmp2)


def GumbelDistributionTest():
	u,beta = 2,4
	gum = GumbelDistribution(u,beta)
	print gum.generate()
	

# 6-5
def CDFexpLamada(x,lamada):
	return -1*math.exp(-1*lamada*x)

def CDFbetweenExpLamada(lamada,x1,x2):
	return CDFexpLamada(lamada,x2)-CDFexpLamada(lamada,x1)

def CDFexpLamadaTest():
	lamada = 2
	x1,x2 = 1,20
	print CDFbetweenExpLamada(lamada,x1,x2)

# 6-6
def BluePeople():
	resp = brfss.Respondents()
	resp.ReadRecords()

	manNum = 0
	for r in resp.records:
		if r.sex == 1:
			manNum += 1
	print manNum
	# manNum = 155703

	manMu,manSigma = 178,59.4
	x1,x2 = 178,185
	p1 = erf.NormalCdf(x1,mu = manMu,sigma = manSigma)
	p2 = erf.NormalCdf(x2,mu = manMu,sigma = manSigma)
	num = (p2-p1)*manNum
	print num
	
# 6-9
def PmfXplusY(pmf_x,pmf_y):
	XplusY = Pmf.Pmf()
	for v1,p1 in pmf_x.Items():
		for v2,p2 in pmf_y.Items():
			XplusY.Incr(v1+v2,p1*p2)
	return XplusY

def PmfMaxofXandY(pmf_x,pmf_y):
	maxofXandY = Pmf.Pmf()
	for v1,p1 in pmf_x.Items():
		for v2,p2 in pmf_y.Items():
			maxofXandY.Incr(v1 if v1>v2 else v2,p1*p2)
	return maxofXandY

def Pmfconvolution():
	l1,l2 = [1,2,3],[2,3,4]
	pmf1 = Pmf.MakePmfFromList(l1)
	pmf2 = Pmf.MakePmfFromList(l2)
	xPlusY = PmfXplusY(pmf1,pmf2)
	print xPlusY.Items()
	maxofXandY = PmfMaxofXandY(pmf1,pmf2)
	print maxofXandY.Items()

# 6-13
def ExpLamadaX(lamada,x):
	return lamada * math.exp(-1*lamada*x)

def CentralLimitTheorem():
	num = 4
	times = 100
	maxX = 2
	lamadas = [i+2 for i in range(num)]
	sumHist = Pmf.Hist()

	for i in range(times):
		sumRes = 0
		x = random.random()*maxX
		for lamada in lamadas:
			sumRes += ExpLamadaX(lamada,x)
			sumHist.Incr(sumRes)

	cdf = Cdf.MakeCdfFromHist(sumHist)

	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show()
	



if __name__ == '__main__':
	# SkewnessTest()
	# Gini()
	# GumbelDistributionTest()
	# CDFexpLamadaTest()
	# BluePeople()
	# PmfXplusY()
	# Pmfconvolution()
	CentralLimitTheorem()
