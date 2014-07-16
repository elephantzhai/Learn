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




def MonteCarloGame():
	MonteCarloGame1()

# 5-5
if __name__  == '__main__':
	# MontyHall()
	# HenriPoincare()
	# DanceWomanHigherThanMan()
	# OneHundredCoin()
	MonteCarloGame()