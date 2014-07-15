import random
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

	

if __name__  == '__main__':
	MontyHall()