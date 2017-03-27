import os
import re
import json
import sys
from random import shuffle
from collections import defaultdict

bias = 0
count=0
beta=0
initialDict = defaultdict(list)
fileDict={}
finalDict=defaultdict(list)

fileList = []


for root, dirs, files in os.walk(sys.argv[1]):
    for i in range(0, len(files)):
        if files[i] not in ['README.md', '.DS_Store', 'README.txt', 'LICENSE','_MACOSX']:
            filename = root + '/' + files[i]
            f = open(filename, 'r', encoding="latin1")
            content = f.read()
            content=content.split()
            fileDict[filename]=content
            f.close()

for j in fileDict:

    for k in range(0, len(fileDict[j])):
        if fileDict[j][k] not in initialDict:
            initialDict[fileDict[j][k]] = [0, 0]
            finalDict[fileDict[j][k]] = [0, 0]


for i in range(0, 30):
    keys = list(fileDict.keys())
    shuffle(keys)
    #print(fileDict)
    for j in fileDict:
        count+=1
        yflag=0
        alpha = 0
        alpha1 = 0
        for i in fileDict[j]:
            alpha1 = alpha1+initialDict[i][0]

                #print(alpha1)
        alpha = alpha1 + bias

        if "spam" in j:
            yflag=1
        elif "ham" in j:
            yflag=-1
        y_alpha= yflag * alpha
        #print(yflag)

        if y_alpha<=0:
            bias = bias + yflag
            beta = beta + (count * yflag)
            for i in fileDict[j]:
                initialDict[i][0] += yflag
                initialDict[i][1] += (count * yflag)


for i in initialDict:
    initialDict[i][1]=initialDict[i][0]-((1/count)*initialDict[i][1])
    finalDict[i][0]=round((initialDict[i][1]),2)
beta=round((bias-((1/count)*beta)),2)
#print(beta)

for i in finalDict:
    finalDict[i][1]=beta


with open('per_model.txt', 'w+', encoding='latin1') as a:
    json.dump(initialDict, a)
    #a.close()

