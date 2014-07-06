import Pmf
import myplot
import urllib
import Cdf
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
 	print 'hi'
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
	if len(t) <6:
		return None
	place, divtot, div, gun, net, pace = t[0:6]

	if '/' not in divtot:
		return None

	for time in [gun, net, pace]:
		if ':' not in time:
			return None
	return place, divtot, div, gun, net, pace

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


if __name__ == "__main__":
	# ClassSize()
	# Relay()
	# Relay_soln()