import math
from string import ascii_lowercase

def idf(termLL, n):
    idfList = {}
    l = len(termLL) - 1
    for i in range(l):
        ni = termLL[i][1]
        tempTerm = termLL[i][0]
        tempIdf = -math.log(ni/n)
        idfList[tempTerm] = tempIdf
    return idfList

def remove_duplicate(irDict):
    for i in irDict:
        temp_links = []
        for j in irDict[i]:
            if j not in temp_links:
                temp_links.append(j)
        irDict[i] = temp_links
    return irDict

def invertIndex(url, tokens, invert_dict):
    for i in tokens:
        if i in invert_dict:
            invert_dict[i].append(url)
        else:
            invert_dict[i] = []
            invert_dict[i].append(url)
    return invert_dict

def intersect(p1,p2):
    answer = []
    i = 0
    j = 0
    while i < len(p1) and j < len(p2):
        if p1[i] == p2[j]:
            answer.append(p1[i])
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1
    return answer

def ini_biGram(someDict):
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            temp = i + j
            someDict[temp] = []
    return someDict

def updateGrams(someDict , someTokens):
    for i in someDict:
        for j in someTokens:
            if i in j:
                someDict[i].append(j)
    return someDict
