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


	
	
# 5-5
if __name__  == '__main__':
	# MontyHall()
	HenriPoincare()