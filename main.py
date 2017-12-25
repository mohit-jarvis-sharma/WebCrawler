import dataConnect
import IR_utils
import json
from urllib.parse import urlparse
from tabulate import tabulate
import pandas as pd

seed = "https://www.python.org/"
limit = 10

counter = 0

linkQueue = []
visited  = []
tdMat = []
temp_links = {}

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
    temp_links[temp_url] = newLinks
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

"""
adj_mat = []
ref_list = list(temp_links.keys())
adj_mat.append(ref_list)

for i in ref_list:
    temp = []
    temp.append(i)
    for j in ref_list:
        if j in temp_links[i]:
            temp.append(1)
        else:
            temp.append(0)
    adj_mat.append(temp)

for i in adj_mat:
    print(i)"""

quiz_adj_mat = []
ref_list = list(temp_links.keys())
quiz_adj_mat.append(['Row Botttom --- Column Right'] + ref_list)

for i in ref_list:
    temp = []
    temp.append(i)
    for j in ref_list:
        if j in temp_links[i]:
            temp1 = urlparse(i)
            dom1 = '{uri.scheme}://{uri.netloc}/'.format(uri=temp1)
            temp2 = urlparse(j)
            dom2 = '{uri.scheme}://{uri.netloc}/'.format(uri=temp2)
            if dom1 == dom2:
                temp.append(0)
            else:
                temp.append(1)
        else:
            temp.append(0)
    quiz_adj_mat.append(temp)

"""
for i in quiz_adj_mat:
    print(i)"""
print(tabulate(quiz_adj_mat))

df = pd.DataFrame(quiz_adj_mat)
df.to_excel('output.xlsx', header=False, index=False)