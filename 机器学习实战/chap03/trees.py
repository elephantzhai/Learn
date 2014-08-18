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

def spiltDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reduceFeatVec = featVec[:axis]
			reduceFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reduceFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFuatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain,bestFeature = 0.0,-1
	for i in range(numFuatures):
		featList = [example[i] for example in dataSet]
		uniqueVals =set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = spiltDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob *calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature


def shannonTest():
	dataSet,labels = creteDataSet()
	print calcShannonEnt(dataSet)
	print spiltDataSet(dataSet,0,1)
	print spiltDataSet(dataSet,0,0)
	print chooseBestFeatureToSplit(dataSet)

def main():
	shannonTest()


if __name__ == "__main__":
	main()
