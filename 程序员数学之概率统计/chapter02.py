import thinkstats
import math
import survey
import Pmf
import operator
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

if __name__ == '__main__':
	# Punpkin()
	# stDevOfBirth()
	# Mode()
	Allmodes()