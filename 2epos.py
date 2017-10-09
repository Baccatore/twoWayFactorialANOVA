#coding: utf-8
# [2-element position DOE]
# Author: Yuichiro SUGA
# Created: 2017-10-05

import os
import statistics as stcs
import csv

NA = 2   # Nb of levels for factor A
NB = 2   # Nb of levels for factor B
R  = 258 # Nb of interation
CT = 0   # Total of squarred sum
SA = 0   # Main effect A
SB = 0   # Main effect B
SAB= 0   # Interaction between A and B
SE = 0   # Sum of errors

#DATA list
#Let A1, A2, B1 and B2
# A1: W/O  electronic field
# A2: With electronic field
# B1: W/O  force field
# B2: With force field
#Also,
#  \ | A1  | A2   
# B1 | X11 | X12  
# B2 | X21 | X22  
class Data :
# Constructor
# condA/B : condition A/B, 0 stands for undefined
    def __init__(self):
        self.data = []
        self.condA = 0
        self.condB = 0
        self.mean = 0
        self.squaredSum = 0
        self.total = 0
    def setData(self, iData):
        self.data = iData
        self.mean = stcs.mean(self.data)
    def addData(self, iData):
        self.data.append(iData)
    def setCond(self, icondA, icondB):
        self.condA = icondA
        self.condB = icondB
    def set(self, iCondA, iCondB, iData):
        self.setData(iData)
        self.setCond(iCondA, iCondB)
    def getMean(self):
        return stcs.mean(self.data)
    def getSum(self):
        return sum(self.data)
    def cal(self):
        R = len(self.data)
        for r in range(R):
            tmp = self.data[r]
            self.squqredSum = self.squaredSum + tmp * tmp
            self.total = self.total + tmp
    def showData(self):
        print(*self.data)

X = [[Data() for i in range(NA)] for j in range(NB)]
if __name__ == '__main__':
    print('\n\nHello, World!')
    print('This program is a statisitiacl analyser')
    print('for 2 way factorial ANOVA')
    print('----------------------\n\n')
    with open('axonlength.csv', newline='',) as datafile:
        rows = csv.reader(datafile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for row in rows:
            for i in range(NA):
                for j in range(NB):
                    X[i][j].addData(row[i+j*NA])
    for i in range(NA):
        for j in range(NB):
            X[i][j].cal()
            print(X[i][j].total)
