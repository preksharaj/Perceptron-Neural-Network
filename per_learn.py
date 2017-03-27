import os
import re
import json
import sys
from random import shuffle
from collections import defaultdict


bias = 0
initialDict = defaultdict(list)
fileDict = {}

fileList = []

for root, dirs, files in os.walk(sys.argv[1]):
    for i in range(0, len(files)):
        if files[i] not in ['README.md', '.DS_Store', 'README.txt', 'LICENSE','_MACOSX']:
            filename = root + '/' + files[i]
            # print(filename)
            f = open(filename, 'r', encoding="latin1")
            content = f.read()
            content = content.split()
            fileDict[filename] = content
            f.close()


for j in fileDict:

    for k in range(0, len(fileDict[j])):
        if fileDict[j][k] not in initialDict:
            initialDict[fileDict[j][k]] = [0, 0]

for i in range(0, 20):
    keys = list(fileDict.keys())
    shuffle(keys)
    # print(fileDict)
    for j in fileDict:
        yflag = 0
        alpha = 0
        alpha1 = 0
        for i in fileDict[j]:
            alpha1 = alpha1 + initialDict[i][0]

            # print(alpha1)
        alpha = alpha1 + bias

        # print(initialDict)
        if "spam" in j:
            yflag = 1
        elif "ham" in j:
            yflag = -1
        y_alpha = yflag * alpha
        # print(yflag)

        if y_alpha <= 0:
            bias = bias + yflag
            for i in fileDict[j]:
                initialDict[i][0] += yflag

for i in initialDict:
    initialDict[i][1] = bias

with open('per_model.txt', 'w+', encoding='latin1') as a:
    json.dump(initialDict, a)
    # a.close()

