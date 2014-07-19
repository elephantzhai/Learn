import survey
import thinkstats
import math
import irs
import Pmf
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
	


	




if __name__ == '__main__':
	# SkewnessTest()
	Gini()