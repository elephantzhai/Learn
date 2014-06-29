# coding=UTF-8
import survey
#1-3 1
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of Pregnancies',len(table.records)

liveOutCome = 0

# 1-3 2
for record in table.records:
	if(record.outcome==1):
		liveOutCome+=1

print "live OutCome",liveOutCome

#1-3 3
firstBirth=0
notFirstBirth=0
for record in table.records:
	if(record.outcome==1):
		if(record.birthord==1):
			firstBirth+=1
		else:
			notFirstBirth+=1

print "firstBirth",firstBirth,"notFirstBirth",notFirstBirth

#1-3 4
firstBirth=0
firstBirthWeek=0
notFirstBirth=0
notFirstBirthWeek=0
for record in table.records:
	if(record.outcome==1):
		if(record.birthord==1):
			firstBirth+=1
			firstBirthWeek+=record.prglength
		else:
			notFirstBirth+=1
			notFirstBirthWeek+=record.prglength
print "firstBirth average:",firstBirthWeek/firstBirth,"notFirstBirth average:",notFirstBirthWeek/notFirstBirth