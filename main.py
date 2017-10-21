import dataConnect
import IR_utils
import json
import math

seed = "https://askubuntu.com/questions/29797/how-can-i-extend-the-desktop-onto-an-external-monitor-projector"
limit = 4

counter = 0

linkQueue = []
visited  = []
tdMat = []

linkQueue.append(seed)
linkCount = 0

irDict = {}
biGram = {}
outDeg = {}

biGram = IR_utils.ini_biGram(biGram)

while counter < limit:
    print("Count " + str(linkCount))
    if linkQueue[linkCount] not in visited:
        temp_url = linkQueue[linkCount]
        visited.append(temp_url)
        linkCount = linkCount + 1
    else:
        linkCount = linkCount + 1
        continue
    try:
        newLinks, newTokens = dataConnect.getData(temp_url)
    except:
        continue
    someNewDeg = len(newLinks)
    outDeg[temp_url] = someNewDeg
    linkQueue.extend(newLinks)
    irDict = IR_utils.invertIndex(temp_url, newTokens, irDict)
    biGram = IR_utils.updateGrams(biGram, newTokens)
    counter = counter + 1

for i in irDict:
    temp = []
    temp.append(i)
    for j in visited:
        if j in irDict[i]:
            temp.append(1)
        else:
            temp.append(0)
    tdMat.append(temp)

irDict = IR_utils.remove_duplicate(irDict)


with open('index.txt', 'w') as file:
     file.write(json.dumps(irDict))

with open('bigram.txt', 'w') as file:
    file.write(json.dumps(biGram))

print(outDeg)