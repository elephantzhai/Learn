# coding=UTF-8
from math import log

def creteDataSet():
	dataSet = [[1,1,'maybe'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],]
	labels = ['no surfacing','flippers']
	return dataSet,labels

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] +=1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob*log(prob,2)
	return shannonEnt

def shannonTest():
	dataSet,labels = creteDataSet()
	print calcShannonEnt(dataSet)

def main():
	shannonTest()


if __name__ == "__main__":
	main()
