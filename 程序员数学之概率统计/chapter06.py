import survey
import thinkstats
import math
# 6-1-1
def Skewness(samples):
	l = len(samples)
	u = sum(samples)*1.0/l
	tmp1,tmp2 = 0,0

	for i in range(l):
		tmp1 += (samples[i]-u)**2
		tmp2 += (samples[i]-u)**3
	m2,m3 = tmp1/l,tmp2/l
	print m2,m3
	g1 = m3/((m2**3)**0.5)
	return g1
# 6-1-2	
def Skewness2():
	table = survey.Pregnancies()
	table.ReadRecords()
	pregLengths = [record.prglength for record in table.records]
	print len(pregLengths)

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
	# Skewness2()
	# PearsonSkewness()
	




if __name__ == '__main__':
	SkewnessTest()