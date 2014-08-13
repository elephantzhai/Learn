# coding=UTF-8
from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels
def classify0(inX,daraSet,labels,k):
	daraSetSize = daraSet.shape[0]

def main():
	group,labels = createDataSet()
	classify0([0,0],group,labels,3)

if __name__ == "__main__":
	main()
