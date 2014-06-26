import thinkstats
import math
import survey
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

if __name__ == '__main__':
	Punpkin()
	stDevOfBirth()