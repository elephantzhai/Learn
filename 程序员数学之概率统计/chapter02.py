import thinkstats
import math
import survey
import Pmf
import operator
import descriptive
import matplotlib.pyplot as pyplot
# 2-1-1
def Punpkin():
	weights = [1,1,1,3,3,591]
	mean = thinkstats.Mean(weights)
	var = thinkstats.Var(weights,mean)
	stDev = math.sqrt(var)
	print "average",mean,"var",var,"stDev",stDev

# 2-2-1
def stDevOfBirth():
	table = survey.Pregnancies()
	table.ReadRecords()
	firstBirth =[]
	notFirstBirth = []

	for record in table.records:
		if(record.outcome==1):
			if(record.birthord==1):
				firstBirth.append(record.prglength)
			else:
				notFirstBirth.append(record.prglength)

				
	firstBirthStDev = math.sqrt(thinkstats.Var(firstBirth))
	notFirstBirthStDev = math.sqrt(thinkstats.Var(notFirstBirth))
	print "firstBirthStDev",firstBirthStDev,"notFirstBirthStDev",notFirstBirthStDev

# 2-3-1
def Mode():
	items = [1,2,3,2,4,1,3,2,4]
	hist = Pmf.MakeHistFromList(items)
	maxFreq=0;maxVal=0;
	for val,freq in hist.Items():
		if(freq>maxFreq):
			maxFreq = freq
			maxVal = val

	print "maxVal",maxVal,"maxFreq",maxFreq
def Allmodes():
	items = [1,2,3,2,4,1,3,2,4]
	hist = Pmf.MakeHistFromList(items)
	print sorted(hist.Items(),key=operator.itemgetter(1),reverse=True)
# 2-4-1
def RemainingLifetime():
	modelItems = [1,1,1,2,2,2,2,3,3,4]
	itemLifeTime = 2
	modelPmf = Pmf.MakePmfFromList(modelItems)
	RemainingLifetimeDict = {}
	for var,freq in modelPmf.Items():
		if(var>itemLifeTime):
			RemainingLifetimeDict[var-itemLifeTime] = freq
			print var,freq
	RemainingLifetimePmf = Pmf.MakePmfFromDict(RemainingLifetimeDict)
	print RemainingLifetimePmf.Items()	
# 2-5
def PmfMean():
	items = [1,1,1,2,2,3,4,4]
	pmf = Pmf.MakePmfFromList(items)
	mean = 0
	for var,freq in pmf.Items():
		mean+=var*freq
	print pmf.Mean(),mean

def PmfVar():
	items = [1,1,1,2,2,3,4,4]
	pmf = Pmf.MakePmfFromList(items)
	mean = pmf.Mean()
	varSum = 0.0
	for var,freq in pmf.Items():
		varSum+=freq*(var-mean)**2
	print pmf.Var(),varSum

# 2-6
def ProbRange(pmf,low,high):
	total = 0.0
	for week in range(low,high+1):
		total += pmf.Prob(week)
	return total

def ProbEarly(pmf):
	return ProbRange(pmf,0,37)

def ProbOnTime(pmf):
	return ProbRange(pmf,38,40)

def ProbLate(pmf):
	return ProbRange(pmf,41,50)

def ComputeRelativeRisk(first_pmf,other_pmf):
	funcs = [ProbEarly,ProbOnTime,ProbLate]
	risks = {}

	print "Prob:"
	for func in funcs:
		for pmf in [first_pmf,other_pmf]:
			risks[func.__name__,pmf.name] = func(pmf)
			print func.__name__,pmf.name,risks[func.__name__,pmf.name]
	
	print "risk ratio (first baby/other baby)"
	for func in funcs:
		ratio = risks[func.__name__,first_pmf.name]/risks[func.__name__,other_pmf.name]
		print "risk ratio:",func.__name__,ratio		

def risk():
	pool,first,other = descriptive.MakeTables()
	ComputeRelativeRisk(first.pmf,other.pmf)

# 2-7
def conditionPmf(pmf,filt_func,name = "conditional"):
	
	cond_pmf = pmf.Copy(name)
	vals = [val for val in pmf.Values() if(filt_func(val))]
	for val in vals:
		cond_pmf.Remove(val)

	cond_pmf.Normalize()
	return cond_pmf


def conditionOnWeeks(pmf,week=39,name = "conditional"):

	def filt_func(x):
		return x < week

	return conditionPmf(pmf,filt_func,name)


def makeFigures(first,other):
	weeks = range(35,46)

	probs = {}
	for table in [first,other]:
		name = table.pmf.name
		probs[name] = []
		for week in weeks:
			cond = conditionOnWeeks(table.pmf,week)
			prob = cond.Prob(week)
			print week, prob, table.pmf.name
			probs[name].append(prob)

	pyplot.clf()
	for name,ps in probs.iteritems():
		pyplot.plot(weeks, ps, label=name)
	pyplot.show()
		


def conditional():
	pool,first,other = descriptive.MakeTables()
	makeFigures(first,other)



			

if __name__ == '__main__':
	# Punpkin()
	# stDevOfBirth()
	# Mode()
	# Allmodes()
	# RemainingLifetime()
	# PmfMean()
	# PmfVar()
	# risk()
	conditional()
