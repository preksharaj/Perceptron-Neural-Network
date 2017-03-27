import os
import json
import sys
import re





with open("per_model.txt", 'r',encoding="latin1") as filein:
    data = json.load(filein)


foutput = open(sys.argv[2], 'w+', encoding='latin1')
def writing():
    if (alpha > 0):
        foutput.write("SPAM ")
    else:
        foutput.write("HAM ")

    foutput.write(os.path.join(root, i) + "\n")


for i in data:
    beta=data[i][1]



for root, dirs, files in os.walk(sys.argv[1]):
    for i in files:

        if i not in ['_MACOSX','README.md', '.DS_Store', 'README.txt', 'LICENSE']:
            with open(os.path.join(root,i), 'r',encoding="latin1") as f:
                alpha = 0
                alpha1 = 0
                content = f.read()

                content = content.lower()
                content = content.split()


                for k in range(0,len(content)):
                    if content[k] in data:
                        alpha1 = alpha1 + data[content[k]][0]
                    else:
                        alpha1 = alpha1 + 0

                alpha = alpha1 + beta
                writing()

               # print(foutput)


foutput.close()



