# 6-1-1
def Skewness(samples):
	l = len(samples)
	u = sum(samples)*1.0/l
	tmp1,tmp2 = 0,0

	for i in range(l):
		tmp1 += (samples[i]-u)**2
		tmp2 += (samples[i]-u)**3
	m2,m3 = tmp1/l,tmp2/l
	g1 = m3/((m2**3)**2)
	return g1

# 6-1-2
def SkewnessTest():
	samples = [2,2,3,4,5,6]
	print Skewness(samples)



if __name__ == '__main__':
	SkewnessTest()