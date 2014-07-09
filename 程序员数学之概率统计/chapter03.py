import Pmf
import myplot
import urllib
import Cdf
import descriptive
import random
# 3-1
def BiasedPmf(pmf,name,invert = False):
	new_pmf = pmf.Copy()
	new_pmf.name = name
	for x,p in new_pmf.Items():
		if invert:
			new_pmf.Mult(x,1.0/x)
		else:
			new_pmf.Mult(x,x)
	new_pmf.Normalize()

	return new_pmf

def UnbasedPmf(pmf,name):
	return BiasedPmf(pmf,name,True)

def ClassSize():
	print 'hello'
	d = {
         7: 8, 
         12: 8, 
         17: 14, 
         22: 4, 
         27: 6, 
         32: 12, 
         37: 8, 
         42: 3, 
         47: 2, 
    }
 	actualPmf = Pmf.MakePmfFromDict(d, 'actual')
 	print 'actual mean:',actualPmf.Mean()
 	print 'actual var:',actualPmf.Var()

 	biased_pmf = BiasedPmf(actualPmf,'oberved')
 	print 'observed mean:',biased_pmf.Mean()
 	print 'observed var:',biased_pmf.Var()

 	unbiased_pmf = UnbasedPmf(biased_pmf,'unbiased')
 	print 'unbiased mean:',unbiased_pmf.Mean()
 	print 'unbiased var:',unbiased_pmf.Var()

 	myplot.Pmfs([actualPmf,biased_pmf])
 	myplot.Show(xlabel = 'ClassSize',ylabel = 'Pmf')

 #3-2-1
def CleanLine(line):
	t = line.split();
	if len(t) <10:
		return None
	place, divtot, div, gun, net, pace, name1,name2 ,age ,sex= t[0:10]

	if '/' not in divtot:
		return None

	for time in [gun, net, pace]:
		if ':' not in time:
			return None
	try:
		int(age)
	except ValueError:
		return None
	
	if not(sex == 'M' or sex == 'F'):
		return None

	return place, divtot, div, gun, net, pace, name1,name2 ,int(age), sex

def ReadResult():
	websiteUrl = 'http://www.coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml'
	result = []
	con = urllib.urlopen(websiteUrl)
	for line in con.fp:
		t = CleanLine(line)
		if t:
			result.append(t)

	return result

def ConvertPaceToSpeed(pace):
	m,s =[int(x) for x in pace.split(':')]
	secs = m*60+s
	speed = 1.0/secs*60*60
	return speed

def GetSpeed(results,column = 5):
	speeds = []
	for t in results:
		pace = t[column]
		speed = ConvertPaceToSpeed(pace)
		speeds.append(speed)

	return speeds

def Relay():
	results = ReadResult()
	speeds = GetSpeed(results)
	speedPmf = Pmf.MakePmfFromList(speeds,'speeds')
 	myplot.Pmf(speedPmf)
 	myplot.Show(title='PMF of running speed',xlabel='speed (mph)',ylabel='probability')
# 3-2-2
def BiasedObserverPmf(pmf,myspeed,name = 'observerd'):
	new_pmf = pmf.Copy(name)
	for speed,prob in pmf.Items():
		new_pmf.Mult(speed,abs(myspeed - speed))
	new_pmf.Normalize()

	return new_pmf


def Relay_soln():
	results = ReadResult()
	speeds = GetSpeed(results)
	actualPmf = Pmf.MakePmfFromList(speeds,'actual')

	observedPmf = BiasedObserverPmf(actualPmf,7.5,'observerd')
	myplot.Clf()
	myplot.Hist(observedPmf)
	myplot.Show(title='PMF of running speed',xlabel='speed (mph)',ylabel='probability')

	observedCdf = Cdf.MakeCdfFromPmf(observedPmf)
	myplot.Clf()
	myplot.Cdf(observedCdf)
	myplot.Show(title='Cdf of running speed',xlabel='speed (mph)',ylabel='probability')

# 3-3	
def PercentileRank(scores,yourScore):
	count = 0
	for score in scores:
		if(score<=yourScore):
			count+=1

	percentile_rank = 100*count/len(scores)
	return percentile_rank

def Percentile1(scores,percentile_rank):
	scores.sort()
	for score in scores:
		if PercentileRank(scores,score)>=percentile_rank:
			return score

def Percentile2(scores,percentile_rank):
	scores.sort()
	index = percentile_rank*(len(scores)-1)/100
	return scores[index]

def Percentile():
	scores = [55,66,77,88,99]
	your_score = 77
	percentile_rank = PercentileRank(scores,your_score)
	print 'PercentileRank',percentile_rank
	print 'Percentile1',Percentile1(scores,percentile_rank)
	print 'Percentile2',Percentile2(scores,percentile_rank)

# 3-6
def BirthCdf():
	pool,first,other = descriptive.MakeTables()
	allCdf = Cdf.MakeCdfFromPmf(pool.pmf)
	firstCdf = Cdf.MakeCdfFromPmf(first.pmf)
	otherCdf = Cdf.MakeCdfFromPmf(other.pmf)

	weight = 39
	print 'all',allCdf.Prob(weight)
	print 'first',firstCdf.Prob(weight)
	print 'other',otherCdf.Prob(weight)
# 3-8
def GetSpeedByRangeAndSex(results,column = 5,lowAge = 0,highAge = 200,ageCloumn = 8,sexRange = None,sexColumn = 9):
	speeds = []
	for t in results:
		age = t[ageCloumn]
		if(age>=lowAge and age<highAge ):
			sex = t[sexColumn]
			if(sexRange and sexRange != sex):
				continue
			pace = t[column]
			speed = ConvertPaceToSpeed(pace)
			speeds.append(speed)

	return speeds

def ColorRunRate():
	results = ReadResult()
	allSpeeds = GetSpeedByRangeAndSex(results)
	m4049Speeds = GetSpeedByRangeAndSex(results,lowAge=40,highAge=50,sexRange = 'M')
	m5059Speeds = GetSpeedByRangeAndSex(results,lowAge=50,highAge=60,sexRange = 'M')
	f2039Speeds = GetSpeedByRangeAndSex(results,lowAge=20,highAge=40,sexRange = 'F')
	allSpeeds.sort()
	m4049Speeds.sort()
	m5059Speeds.sort()
	f2039Speeds.sort()

	print len(results),len(allSpeeds),len(m4049Speeds),len(m5059Speeds),len(f2039Speeds)
	allCdf = Cdf.MakeCdfFromList(allSpeeds)
	m4049Cdf = Cdf.MakeCdfFromList(m4049Speeds)
	m5059Cdf = Cdf.MakeCdfFromList(m5059Speeds)
	f2039Cdf = Cdf.MakeCdfFromList(f2039Speeds)

	pecAll =  allCdf.Prob(allSpeeds[96])
	pec4049 = m4049Cdf.Prob(m4049Speeds[26])
	speedAfter10 = m5059Cdf.Value(pec4049)
	studentGirlSpeed = f2039Cdf.Value(pec4049)
	
	print 'pec in all age',(1-pecAll)*100
	print 'pec in 40-49',(1-pec4049)*100
	print 'speed in 50-59',speedAfter10
	print 'speed in 20-39',studentGirlSpeed
# 3-9
def Sample(cdf,n):
	randoms = []
	for i in range(n):
		randoms.append(cdf.Value(random.random()))
	return randoms

def ResambleBirth():
	pool,first,other = descriptive.MakeTables()
	allCdf = Cdf.MakeCdfFromPmf(pool.pmf)
	randomCdf = Cdf.MakeCdfFromList(Sample(allCdf,1000))
	randomCdf.name = 'random birth'

	myplot.Clf()
	myplot.Cdfs([allCdf,randomCdf])
	myplot.show()

def Random():
	list1 =[1,2,3,4,5]
	cdf = Cdf.MakeCdfFromList(list1)
	print Sample(cdf,4) 
	ResambleBirth()

# 3-10
def Random100():
	results = []
	for i in range(1000):
		results.append(random.random())
	pmf = Pmf.MakePmfFromList(results)
	cdf = Cdf.MakeCdfFromPmf(pmf)

	myplot.Clf()
	myplot.Pmf(pmf)
	myplot.show()

	myplot.Clf()
	myplot.Cdf(cdf)
	myplot.show()
# 3-11
def Median(cdf):
	return cdf.Value(0.5)

def InterquartileRange(cdf):
	return cdf.Value(0.75)-cdf.Value(0.25)

def MedianAndInterquartileRange():
	pool,first,other = descriptive.MakeTables()
	allCdf = Cdf.MakeCdfFromPmf(pool.pmf)
	print Median(allCdf)
	print InterquartileRange(allCdf)


if __name__ == "__main__":
	# ClassSize()
	# Relay()
	# Relay_soln()
	# Percentile()
	# BirthCdf()
	# ColorRunRate()
	# Random()
	# Random100()
	MedianAndInterquartileRange()


