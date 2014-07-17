import random
import erf
import thinkstats
import math
import Cdf
import myplot
import Pmf
# 5-4
def MontyHall():
	numA,numB = 0,0
	for i in range(10000):
		index = int(random.random()*3)
		if index==2:
			index =1

		if index == 0:
			numA+=1
		else:
			numB+=1
	print numA,numB

# 5-5
def HenriPoincare():
	ave = 950
	sigma = 50
	weights = []
	days= 360
	n = 4
	for i in range(days):
		p = 0.0
		for j in range(n):
			temp = random.random()
			if p<temp:
				p = temp
		weights.append(erf.NormalCdfInverse(p,mu=ave,sigma = sigma))
	mu, var = thinkstats.MeanVar(weights)
	print mu,math.sqrt(var)

	normal = []
	for i in range(1000):
		normal.append(erf.NormalCdfInverse(random.random(),mu = mu,sigma = math.sqrt(var)))
	# histReal = Pmf.MakeHistFromList(weights,'real')
	# histStand = Pmf.MakeHistFromList(normal,'stand')
	# pmfReal = Pmf.MakePmfFromList(weights,"real")
	# pmfStand = Pmf.MakePmfFromList(normal,'stand')
	cdfReal = Cdf.MakeCdfFromList(weights)
	cdfStand = Cdf.MakeCdfFromList(normal)

	myplot.Clf()
	# myplot.Hists([histReal,histStand])
	myplot.Cdfs([cdfReal,cdfStand])
	# myplot.Pmfs([pmfReal,pmfStand])
	myplot.show()


# 5-7
def DanceWomanHigherThanMan():
	uMan,varMan = 178 ,59.4
	uWoman,varWoman = 163,52.8
	sigmaMan = math.sqrt(varMan)
	sigmaWoman = math.sqrt(varWoman)

	n = 1000
	nMan,nWoman = 0,0

	for i in range(n):
		pMan = random.random()
		pWoman = random.random()
		hMan = erf.NormalCdfInverse(pMan,mu = uMan,sigma = sigmaMan)
		hWoman = erf.NormalCdfInverse(pWoman,mu = uWoman,sigma = sigmaWoman)
		if hMan>hWoman:
			nMan+=1
		else:
			nWoman+=1

	print nMan,nWoman

# 5-10
def OneHundredCoin():
	p = thinkstats.Binom(n=100,k=50)*(0.5**50)*((1-0.5)**50)
	print p

# 5-11
def MonteCarloGame1():
	gameTimes = 100
	playerNum = 10
	playTimes = 15

	game10 = 0
	for i in range(gameTimes):
		player10 = 0
		for j in range(playerNum):
			n = 0
			for k in range(playTimes):
				if random.random()>0.5:
					n+=1
			if n==10:
				player10+=1
				continue
		if player10>0:
			game10+=1
	print game10,gameTimes

def MonteCarloGame2():
	testTimes = 200
	gameTimes = 82
	playerNum = 10
	playTimes = 15
	continueNum = 10
	contineuCount = 0
	for t in range(testTimes):
		isSee = False
		for i in range(gameTimes):
			for j in range(playerNum):
				# result = [random.random()>0.5 for k in range(playTimes)]
				isInState = None
				num = 0
				for k in range(playTimes):
					p = random.random()>0.5
					if num == 0:
						isInState = p
						num =1
					else:
						if isInState == p:
							num+=1
						else:
							if num == continueNum:
								isSee = True
								continue
							else:
								if playTimes-k<continueNum:
									continue
								else:
									isInState = p
									num = 1
				if num == continueNum:
					isSee = True
				if isSee:
					continue
			if isSee:
				continue
		if isSee:
			contineuCount+=1
	print contineuCount,testTimes



def MonteCarloGame():
	# MonteCarloGame1()
	MonteCarloGame2()

# 5-13
def CancerTest1():
	totalList = []
	total = 0
	year = 10
	peopleNum = 1000
	p = 0.001
	for i in range(year):
		new = 0
		for j in range(peopleNum):
			if random.random()<p:
				new+=1
		peopleNum -= new
		total += new
		totalList.append(total)
	print totalList
def CancerTest2():
	total = 0
	year = 10
	peopleNum = 100
	p = 0.05
	for i in range(year):
		new = 0
		for j in range(peopleNum):
			if random.random()<p:
				new+=1
		peopleNum -= new
		total += new
	print total

def CancerTest3():
	
	year = 10
	peopleNum = 100
	pCancer = 0.001
	pWatch = 0.02
	groupNum = 100
	groupCount = 0

	for k in range(groupNum):
		total = 0
		tempPeople = peopleNum
		for i in range(year):
			new = 0
			for j in range(tempPeople):
				if random.random()<pCancer:
					new+=1
			tempPeople -= new
			total += new
		if total>= pWatch*peopleNum:
			groupCount+=1
	print groupCount,groupNum



def CancerTest():
	# CancerTest1()
	# CancerTest2()
	CancerTest3()

# 5-14
def UseMedicalRate():
	medicalUseRate = 0.05
	sensetive = 0.6
	special = 0.99

	realRate = medicalUseRate*sensetive/(sensetive*medicalUseRate+(1-special)*(1-medicalUseRate))
	print realRate

# 5-15
def MMchocolate():
	print 0.5*0.2/(0.2*0.5+0.14*0.5)

if __name__  == '__main__':
	# MontyHall()
	# HenriPoincare()
	# DanceWomanHigherThanMan()
	# OneHundredCoin()
	# MonteCarloGame()
	# CancerTest()
	# UseMedicalRate()
	MMchocolate()