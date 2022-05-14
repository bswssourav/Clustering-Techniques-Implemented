import numpy as np
import pandas as pd
from itertools import groupby
import collections
import networkx as nx
import matplotlib.pyplot as plt


#****----------Single Link Function start---------------------------*****

def singleLink(df):
        #r1 = set(df[0][2])
        #print(r1)
        w, h = len(df), len(df);
        similarMatrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(0,len(df)):
            for j in range(0,len(df)):
                similarMatrix[i][j]=-1

        for i in range(0,len(df)):
            for j in range(0,len(df)):

                if (i<j):
                    l1=df.iloc[i][2].split('\n')
                    l2=df.iloc[j][2].split('\n')
                    r1 = set(l1)
                    r2 = set(l2)
                    intersection_len = len(r1.intersection(r2))
                    union_len = len(r1) + len(r2) - intersection_len
                    jaccard = intersection_len / union_len
                    similarMatrix[j][i]=jaccard
                    #print("jaccard of ",i ," and ",j, " is ", jaccard)
                if(i==j):
                    similarMatrix[i][j] = -1

        print(similarMatrix)
        clusterMatrix1 = []
        clusterMatrix2 = []
        clusterMatrix3=  []
        clusterMatrix4 = []
        clusterMatrix5 = []
        clusterMatrix6 = []
        clusterMatrix7 = []
        clusterMatrix8 = []
        clusterMatrix9 = []



        #....................Creating Cluster using Single Link Start..........................#
        clusterCount = len(df)
        while(clusterCount>=9):
            flag=0
            max = 0
            first=-9
            second=-9



            for i in range(0,len(df)):
                for j in range(0,len(df)):

                    if(max<similarMatrix[i][j]):
                        flag=1
                        max=similarMatrix[i][j]
                        first=i
                        second=j
            similarMatrix[first][second]=-1
            if(clusterCount==len(df)):
                clusterMatrix1.append(first)
                clusterMatrix1.append(second)
                for i in range(0, len(df)):
                    maximum = -100
                    for j in range(0, len(clusterMatrix1)):
                        # print("j====",j)
                        if (similarMatrix[clusterMatrix1[j]][i] > maximum):
                            maximum = similarMatrix[clusterMatrix1[j]][i]
                    for k in range(0, len(clusterMatrix1)):
                        similarMatrix[clusterMatrix1[k]][i] = maximum
                clusterCount = clusterCount - len(clusterMatrix1)+1
            if(flag==1):
                if  clusterMatrix1:
                    if first not in clusterMatrix1 and second in clusterMatrix1:
                        clusterMatrix1.append(first)
                        clusterCount = clusterCount - 1
                        for i in range(0, len(df)):
                            maximum = -100
                            for j in range(0, len(clusterMatrix1)):
                                # print("j====",j)
                                if (similarMatrix[clusterMatrix1[j]][i] > maximum):
                                    maximum = similarMatrix[clusterMatrix1[j]][i]
                            for k in range(0, len(clusterMatrix1)):
                                similarMatrix[clusterMatrix1[k]][i] = maximum
                    if second not in clusterMatrix1 and first in clusterMatrix1:
                        clusterMatrix1.append(second)
                        clusterCount = clusterCount - 1
                        for i in range(0, len(df)):
                            maximum = -100
                            for j in range(0, len(clusterMatrix1)):
                                # print("j====",j)
                                if (similarMatrix[clusterMatrix1[j]][i] > maximum):
                                    maximum = similarMatrix[clusterMatrix1[j]][i]
                            for k in range(0, len(clusterMatrix1)):
                                similarMatrix[clusterMatrix1[k]][i] = maximum

                    if clusterMatrix1 and first not in clusterMatrix1 and second not in clusterMatrix1:
                        if not clusterMatrix2:
                            clusterMatrix2.append(first)
                            clusterMatrix2.append(second)
                            clusterCount = clusterCount - len(clusterMatrix2)+1
                            for i in range(0, len(df)):
                                maximum = -100
                                for j in range(0, len(clusterMatrix2)):
                                    # print("j====",j)
                                    if (similarMatrix[clusterMatrix2[j]][i] > maximum):
                                        maximum = similarMatrix[clusterMatrix2[j]][i]
                                for k in range(0, len(clusterMatrix1)):
                                    similarMatrix[clusterMatrix2[k]][i] = maximum
                        else:
                            if first not in clusterMatrix2 and second in clusterMatrix2:
                                clusterMatrix2.append(first)
                                clusterCount = clusterCount - 1
                                for i in range(0, len(df)):
                                    maximum = -100
                                    for j in range(0, len(clusterMatrix2)):
                                        # print("j====",j)
                                        if (similarMatrix[clusterMatrix2[j]][i] > maximum):
                                            maximum = similarMatrix[clusterMatrix2[j]][i]
                                    for k in range(0, len(clusterMatrix2)):
                                        similarMatrix[clusterMatrix2[k]][i] = maximum
                            if second not in clusterMatrix2 and first in clusterMatrix2:
                                clusterMatrix2.append(second)
                                clusterCount = clusterCount - 1
                                for i in range(0, len(df)):
                                    maximum = -100
                                    for j in range(0, len(clusterMatrix2)):
                                        # print("j====",j)
                                        if (similarMatrix[clusterMatrix2[j]][i] > maximum):
                                            maximum = similarMatrix[clusterMatrix2[j]][i]
                                    for k in range(0, len(clusterMatrix2)):
                                        similarMatrix[clusterMatrix2[k]][i] = maximum
                        if clusterMatrix2 and first not in clusterMatrix2 and second not in clusterMatrix2 :
                            if not clusterMatrix3:
                                clusterMatrix3.append(first)
                                clusterMatrix3.append(second)
                                for i in range(0, len(df)):
                                    maximum = -100
                                    for j in range(0, len(clusterMatrix3)):
                                        # print("j====",j)
                                        if (similarMatrix[clusterMatrix3[j]][i] > maximum):
                                            maximum = similarMatrix[clusterMatrix3[j]][i]
                                    for k in range(0, len(clusterMatrix3)):
                                        similarMatrix[clusterMatrix3[k]][i] = maximum
                                clusterCount = clusterCount - len(clusterMatrix3) + 1
                            else:
                                if first not in clusterMatrix3 and second in clusterMatrix3:
                                    clusterMatrix3.append(first)
                                    clusterCount = clusterCount - 1
                                    for i in range(0, len(df)):
                                        maximum = -100
                                        for j in range(0, len(clusterMatrix3)):
                                            # print("j====",j)
                                            if (similarMatrix[clusterMatrix3[j]][i] > maximum):
                                                maximum = similarMatrix[clusterMatrix3[j]][i]
                                        for k in range(0, len(clusterMatrix3)):
                                            similarMatrix[clusterMatrix3[k]][i] = maximum
                                if second not in clusterMatrix3 and first in clusterMatrix3:
                                    clusterMatrix3.append(second)
                                    clusterCount = clusterCount - 1
                                    for i in range(0, len(df)):
                                        maximum = -100
                                        for j in range(0, len(clusterMatrix3)):
                                            # print("j====",j)
                                            if (similarMatrix[clusterMatrix3[j]][i] > maximum):
                                                maximum = similarMatrix[clusterMatrix3[j]][i]
                                        for k in range(0, len(clusterMatrix3)):
                                            similarMatrix[clusterMatrix3[k]][i] = maximum
                            if clusterMatrix3 and first not in clusterMatrix3 and second not in clusterMatrix3:
                                if not clusterMatrix4:
                                    clusterMatrix4.append(first)
                                    clusterMatrix4.append(second)
                                    clusterCount = clusterCount - len(clusterMatrix4) + 1
                                    for i in range(0, len(df)):
                                        maximum = -100
                                        for j in range(0, len(clusterMatrix4)):
                                            # print("j====",j)
                                            if (similarMatrix[clusterMatrix4[j]][i] > maximum):
                                                maximum = similarMatrix[clusterMatrix4[j]][i]
                                        for k in range(0, len(clusterMatrix4)):
                                            similarMatrix[clusterMatrix4[k]][i] = maximum
                                else:
                                    if first not in clusterMatrix4 and second in clusterMatrix4:
                                        clusterMatrix4.append(first)
                                        clusterCount = clusterCount - 1
                                        for i in range(0, len(df)):
                                            maximum = -100
                                            for j in range(0, len(clusterMatrix4)):
                                                # print("j====",j)
                                                if (similarMatrix[clusterMatrix4[j]][i] > maximum):
                                                    maximum = similarMatrix[clusterMatrix4[j]][i]
                                            for k in range(0, len(clusterMatrix4)):
                                                similarMatrix[clusterMatrix4[k]][i] = maximum
                                    if second not in clusterMatrix4 and first in clusterMatrix4:
                                        clusterMatrix4.append(second)
                                        clusterCount = clusterCount - 1
                                        for i in range(0, len(df)):
                                            maximum = -100
                                            for j in range(0, len(clusterMatrix4)):
                                                # print("j====",j)
                                                if (similarMatrix[clusterMatrix4[j]][i] > maximum):
                                                    maximum = similarMatrix[clusterMatrix4[j]][i]
                                            for k in range(0, len(clusterMatrix4)):
                                                similarMatrix[clusterMatrix4[k]][i] = maximum
                                if clusterMatrix4 and first not in clusterMatrix4 and second not in clusterMatrix4:
                                    if not clusterMatrix5:
                                        clusterMatrix5.append(first)
                                        clusterMatrix5.append(second)
                                        clusterCount=clusterCount-len(clusterMatrix5)+1
                                        for i in range(0, len(df)):
                                            maximum = -100
                                            for j in range(0, len(clusterMatrix5)):
                                                # print("j====",j)
                                                if (similarMatrix[clusterMatrix5[j]][i] > maximum):
                                                    maximum = similarMatrix[clusterMatrix5[j]][i]
                                            for k in range(0, len(clusterMatrix5)):
                                                similarMatrix[clusterMatrix5[k]][i] = maximum
                                    else:
                                        if first not in clusterMatrix5 and second in clusterMatrix5:
                                            clusterMatrix5.append(first)
                                            clusterCount = clusterCount - 1
                                            for i in range(0, len(df)):
                                                maximum = -100
                                                for j in range(0, len(clusterMatrix5)):
                                                    # print("j====",j)
                                                    if (similarMatrix[clusterMatrix5[j]][i] > maximum):
                                                        maximum = similarMatrix[clusterMatrix5[j]][i]
                                                for k in range(0, len(clusterMatrix5)):
                                                    similarMatrix[clusterMatrix5[k]][i] = maximum
                                        if second not in clusterMatrix5 and first in clusterMatrix5:
                                            clusterMatrix5.append(second)
                                            clusterCount = clusterCount - 1
                                            for i in range(0, len(df)):
                                                maximum = -100
                                                for j in range(0, len(clusterMatrix5)):
                                                    # print("j====",j)
                                                    if (similarMatrix[clusterMatrix5[j]][i] > maximum):
                                                        maximum = similarMatrix[clusterMatrix5[j]][i]
                                                for k in range(0, len(clusterMatrix5)):
                                                    similarMatrix[clusterMatrix5[k]][i] = maximum
                                    if clusterMatrix5 and first not in clusterMatrix5 and second not in clusterMatrix5:
                                        if not clusterMatrix6:
                                            clusterMatrix6.append(first)
                                            clusterMatrix6.append(second)
                                            clusterCount = clusterCount - len(clusterMatrix6) + 1
                                            for i in range(0, len(df)):
                                                maximum = -100
                                                for j in range(0, len(clusterMatrix6)):
                                                    # print("j====",j)
                                                    if (similarMatrix[clusterMatrix6[j]][i] > maximum):
                                                        maximum = similarMatrix[clusterMatrix6[j]][i]
                                                for k in range(0, len(clusterMatrix6)):
                                                    similarMatrix[clusterMatrix6[k]][i] = maximum
                                        else:
                                            if first not in clusterMatrix6 and second in clusterMatrix6:
                                                clusterMatrix6.append(first)
                                                clusterCount=clusterCount-1
                                                for i in range(0, len(df)):
                                                    maximum = -100
                                                    for j in range(0, len(clusterMatrix6)):
                                                        # print("j====",j)
                                                        if (similarMatrix[clusterMatrix6[j]][i] > maximum):
                                                            maximum = similarMatrix[clusterMatrix6[j]][i]
                                                    for k in range(0, len(clusterMatrix6)):
                                                        similarMatrix[clusterMatrix6[k]][i] = maximum
                                            if second not in clusterMatrix6 and first in clusterMatrix6:
                                                clusterMatrix6.append(second)
                                                clusterCount=clusterCount-1
                                                for i in range(0, len(df)):
                                                    maximum = -100
                                                    for j in range(0, len(clusterMatrix6)):
                                                        # print("j====",j)
                                                        if (similarMatrix[clusterMatrix6[j]][i] > maximum):
                                                            maximum = similarMatrix[clusterMatrix6[j]][i]
                                                    for k in range(0, len(clusterMatrix6)):
                                                        similarMatrix[clusterMatrix6[k]][i] = maximum
                                        if clusterMatrix6 and first not in clusterMatrix6 and second not in clusterMatrix6:
                                            if not clusterMatrix7:
                                                clusterMatrix7.append(first)
                                                clusterMatrix7.append(second)
                                                clusterCount = clusterCount - len(clusterMatrix7) + 1
                                                for i in range(0, len(df)):
                                                    maximum = -100
                                                    for j in range(0, len(clusterMatrix7)):
                                                        # print("j====",j)
                                                        if (similarMatrix[clusterMatrix7[j]][i] > maximum):
                                                            maximum = similarMatrix[clusterMatrix7[j]][i]
                                                    for k in range(0, len(clusterMatrix7)):
                                                        similarMatrix[clusterMatrix7[k]][i] = maximum
                                            else:
                                                if first not in clusterMatrix7 and second in clusterMatrix7:
                                                    clusterMatrix7.append(first)
                                                    clusterCount=clusterCount-1
                                                    for i in range(0, len(df)):
                                                        maximum = -100
                                                        for j in range(0, len(clusterMatrix7)):
                                                            # print("j====",j)
                                                            if (similarMatrix[clusterMatrix7[j]][i] > maximum):
                                                                maximum = similarMatrix[clusterMatrix7[j]][i]
                                                        for k in range(0, len(clusterMatrix7)):
                                                            similarMatrix[clusterMatrix7[k]][i] = maximum
                                                if second not in clusterMatrix7 and first in clusterMatrix7:
                                                    clusterMatrix7.append(second)
                                                    clusterCount=clusterCount-1
                                                    for i in range(0, len(df)):
                                                        maximum = -100
                                                        for j in range(0, len(clusterMatrix7)):
                                                            # print("j====",j)
                                                            if (similarMatrix[clusterMatrix7[j]][i] > maximum):
                                                                maximum = similarMatrix[clusterMatrix7[j]][i]
                                                        for k in range(0, len(clusterMatrix7)):
                                                            similarMatrix[clusterMatrix7[k]][i] = maximum
                                            if clusterMatrix7 and first not in clusterMatrix7 and second not in clusterMatrix7:
                                                if not clusterMatrix8:
                                                    clusterMatrix8.append(first)
                                                    clusterMatrix8.append(second)
                                                    clusterCount = clusterCount - len(clusterMatrix8) + 1
                                                    for i in range(0, len(df)):
                                                        maximum = -100
                                                        for j in range(0, len(clusterMatrix8)):
                                                            # print("j====",j)
                                                            if (similarMatrix[clusterMatrix8[j]][i] > maximum):
                                                                maximum = similarMatrix[clusterMatrix8[j]][i]
                                                        for k in range(0, len(clusterMatrix8)):
                                                            similarMatrix[clusterMatrix8[k]][i] = maximum
                                                else:
                                                    if first not in clusterMatrix8 and second in clusterMatrix8:
                                                        clusterMatrix8.append(first)
                                                        clusterCount=clusterCount-1
                                                        for i in range(0, len(df)):
                                                            maximum = -100
                                                            for j in range(0, len(clusterMatrix8)):
                                                                # print("j====",j)
                                                                if (similarMatrix[clusterMatrix8[j]][i] > maximum):
                                                                    maximum = similarMatrix[clusterMatrix8[j]][i]
                                                            for k in range(0, len(clusterMatrix8)):
                                                                similarMatrix[clusterMatrix8[k]][i] = maximum
                                                    if second not in clusterMatrix8 and first in clusterMatrix8:
                                                        clusterMatrix8.append(second)
                                                        clusterCount=clusterCount-1
                                                        for i in range(0, len(df)):
                                                            maximum = -100
                                                            for j in range(0, len(clusterMatrix8)):
                                                                # print("j====",j)
                                                                if (similarMatrix[clusterMatrix8[j]][i] > maximum):
                                                                    maximum = similarMatrix[clusterMatrix8[j]][i]
                                                            for k in range(0, len(clusterMatrix8)):
                                                                similarMatrix[clusterMatrix8[k]][i] = maximum
                                                if clusterMatrix8 and first not in clusterMatrix8 and second not in clusterMatrix8:
                                                    if not clusterMatrix9:
                                                        clusterMatrix9.append(first)
                                                        clusterMatrix9.append(second)
                                                        clusterCount = clusterCount - len(clusterMatrix9) + 1
                                                        for i in range(0, len(df)):
                                                            maximum = -100
                                                            for j in range(0, len(clusterMatrix9)):
                                                                # print("j====",j)
                                                                if (similarMatrix[clusterMatrix9[j]][i] > maximum):
                                                                    maximum = similarMatrix[clusterMatrix9[j]][i]
                                                            for k in range(0, len(clusterMatrix9)):
                                                                similarMatrix[clusterMatrix9[k]][i] = maximum
                                                    else:
                                                        if first not in clusterMatrix9 and second in clusterMatrix9:
                                                            clusterMatrix9.append(first)
                                                            clusterCount=clusterCount-1
                                                            for i in range(0, len(df)):
                                                                maximum = -100
                                                                for j in range(0, len(clusterMatrix9)):
                                                                    # print("j====",j)
                                                                    if (similarMatrix[clusterMatrix9[j]][i] > maximum):
                                                                        maximum = similarMatrix[clusterMatrix9[j]][i]
                                                                for k in range(0, len(clusterMatrix9)):
                                                                    similarMatrix[clusterMatrix9[k]][i] = maximum
                                                        if second not in clusterMatrix9 and first in clusterMatrix9:
                                                            clusterMatrix9.append(second)
                                                            clusterCount=clusterCount-1
                                                            for i in range(0, len(df)):
                                                                maximum = -100
                                                                for j in range(0, len(clusterMatrix9)):
                                                                    # print("j====",j)
                                                                    if (similarMatrix[clusterMatrix9[j]][i] > maximum):
                                                                        maximum = similarMatrix[clusterMatrix9[j]][i]
                                                                for k in range(0, len(clusterMatrix9)):
                                                                    similarMatrix[clusterMatrix9[k]][i] = maximum


            #print(clusterMatrix1[1])
            #print(similarMatrix[30][1])
            """for i in range (0,len(df)):
                minimum=100
                for j in range (0,len(clusterMatrix1)):
                    #print("j====",j)
                    if (similarMatrix[clusterMatrix1[j]][i]<minimum):
                        minimum=similarMatrix[clusterMatrix1[j]][i]
                for k in range (0,len(clusterMatrix1)):
                     similarMatrix[clusterMatrix1[k]][i]=minimum"""


            #print(clusterMatrix1)
        print("single Link cluster 1 ===",clusterMatrix1)
        print("single Link cluster 2==",clusterMatrix2)
        print("single Link cluster 3==",clusterMatrix3)
        print("single Link cluster 4==",clusterMatrix4)
        print("single Link cluster 5===",clusterMatrix5)
        print("single Link cluster 6==",clusterMatrix6)
        print("single Link cluster 7==", clusterMatrix7)
        print("single Link cluster 8==", clusterMatrix8)
        print("single Link cluster 9==", clusterMatrix9)

        print("single Link cluster 1 length ===", len(clusterMatrix1))
        print("single Link cluster 2 length==", len(clusterMatrix2))
        print("single Link cluster 3 length==", len(clusterMatrix3))
        print("single Link cluster 4 length==", len(clusterMatrix4))
        print("single Link cluster 5 length===", len(clusterMatrix5))
        print("single Link cluster 6 length==", len(clusterMatrix6))
        print("single Link cluster 7 length==", len(clusterMatrix7))
        print("single Link cluster 8 length==", len(clusterMatrix8))
        print("single Link cluster 9 length==", len(clusterMatrix9))




        # ....................Creating Cluster using Single Link  End ..........................#
        ###NMI VALUE CalCulation.......................................

        countElementsCluster = []
        countElementsCluster.append(len(clusterMatrix1))
        countElementsCluster.append(len(clusterMatrix2))
        countElementsCluster.append(len(clusterMatrix3))
        countElementsCluster.append(len(clusterMatrix4))
        countElementsCluster.append(len(clusterMatrix5))
        countElementsCluster.append(len(clusterMatrix6))
        countElementsCluster.append(len(clusterMatrix7))
        countElementsCluster.append(len(clusterMatrix8))
        countElementsCluster.append(len(clusterMatrix9))



        highLevelDomain = []
        for i in range(0, len(df)):
            highLevelDomain.append(df.iloc[i][3])

        print(len(highLevelDomain))

        counter = collections.Counter(highLevelDomain)
        frequency = list(counter.values())
        uniquehighLevelDomain = list(set(highLevelDomain))
        print(uniquehighLevelDomain)
        print(frequency)
        entropyClass = 0
        entropyCluster=0
        entropyCluster1=0
        entropyCluster2=0
        entropyCluster3=0
        entropyCluster4=0
        entropyCluster5=0
        entropyCluster6=0
        entropyCluster7=0
        entropyCluster8=0
        entropyCluster9=0
        for i in range(0, len(frequency)):
            frac1 = frequency[i] / 150
            entropyClass = entropyClass + (-frac1 * np.log2(frac1))
        print("entrophy of Class:",entropyClass)
        for i in range(0,9):
            frac2 =  countElementsCluster[i]/ 150
            entropyCluster = entropyCluster + (-frac2 * np.log2(frac2))
        print("entrophy of cluster:",entropyCluster)


        cluster1High=[]
        for i in range (0,len(clusterMatrix1)):
            cluster1High.append(df.iloc[clusterMatrix1[i]][3])
        print("cluster1High-------------",cluster1High)
        counterCluster1 = collections.Counter(cluster1High)
        frequencyCluster1 = list(counterCluster1.values())
        for i in range(0, len(frequencyCluster1)):
            frac3 = frequencyCluster1[i] / len(clusterMatrix1)
            entropyCluster1 = entropyCluster1 + (-frac3* np.log2(frac3))
        entropyCluster1=(1/2)*entropyCluster1
        print("entrophy of cluster 1:", entropyCluster1)

        cluster2High = []
        for i in range(0, len(clusterMatrix2)):
            cluster2High.append(df.iloc[clusterMatrix2[i]][3])
        print("cluster2High-------------", cluster2High)
        counterCluster2 = collections.Counter(cluster2High)
        frequencyCluster2 = list(counterCluster2.values())
        print("frequency of cluster 2:", frequencyCluster2)
        for i in range(0, len(frequencyCluster2)):
            frac4 = frequencyCluster2[i] / len(clusterMatrix2)
            entropyCluster2 = entropyCluster2 + (-frac4 * np.log2(frac4))
            #print("entrophy of cluster 2:", entropyCluster2)
        entropyCluster2 = (1 / 2) * entropyCluster2
        print("entrophy of cluster 2:", entropyCluster2)

        cluster3High = []
        for i in range(0, len(clusterMatrix3)):
            cluster3High.append(df.iloc[clusterMatrix3[i]][3])
        print("cluster3High-------------", cluster3High)
        counterCluster3 = collections.Counter(cluster3High)
        frequencyCluster3 = list(counterCluster3.values())
        print("frequency of cluster 3:", frequencyCluster3)
        for i in range(0, len(frequencyCluster3)):
            frac5 = frequencyCluster3[i] / len(clusterMatrix3)
            entropyCluster3 = entropyCluster3 + (-frac5 * np.log2(frac5))
            #print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster3 = (1 / 2) * entropyCluster3
        print("entrophy of cluster 3:", entropyCluster3)

        cluster4High = []
        for i in range(0, len(clusterMatrix4)):
            cluster4High.append(df.iloc[clusterMatrix4[i]][3])
        print("cluster4High-------------", cluster4High)
        counterCluster4 = collections.Counter(cluster4High)
        frequencyCluster4 = list(counterCluster4.values())
        print("frequency of cluster 4:", frequencyCluster4)
        for i in range(0, len(frequencyCluster4)):
            frac6 = frequencyCluster4[i] / len(clusterMatrix4)
            entropyCluster4 = entropyCluster4 + (-frac6 * np.log2(frac6))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster4 = (1 / 2) * entropyCluster4
        print("entrophy of cluster 4:", entropyCluster4)

        cluster5High = []
        for i in range(0, len(clusterMatrix5)):
            cluster5High.append(df.iloc[clusterMatrix5[i]][3])
        print("cluster5High-------------", cluster5High)
        counterCluster5 = collections.Counter(cluster5High)
        frequencyCluster5 = list(counterCluster5.values())
        print("frequency of cluster 5:", frequencyCluster5)
        for i in range(0, len(frequencyCluster5)):
            frac7 = frequencyCluster5[i] / len(clusterMatrix5)
            entropyCluster5 = entropyCluster5 + (-frac7 * np.log2(frac7))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster5 = (1 / 2) * entropyCluster5
        print("entrophy of cluster 5:", entropyCluster5)

        cluster6High = []
        for i in range(0, len(clusterMatrix6)):
            cluster6High.append(df.iloc[clusterMatrix6[i]][3])
        print("cluster5High-------------", cluster6High)
        counterCluster6 = collections.Counter(cluster6High)
        frequencyCluster6 = list(counterCluster6.values())
        print("frequency of cluster 6:", frequencyCluster6)
        for i in range(0, len(frequencyCluster6)):
            frac8 = frequencyCluster6[i] / len(clusterMatrix6)
            entropyCluster6 = entropyCluster6 + (-frac8 * np.log2(frac8))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster6 = (1 / 2) * entropyCluster6
        print("entrophy of cluster 6:", entropyCluster6)

        cluster7High = []
        for i in range(0, len(clusterMatrix7)):
            cluster7High.append(df.iloc[clusterMatrix7[i]][3])
        print("cluster5High-------------", cluster7High)
        counterCluster7 = collections.Counter(cluster7High)
        frequencyCluster7 = list(counterCluster7.values())
        print("frequency of cluster 7:", frequencyCluster7)
        for i in range(0, len(frequencyCluster7)):
            frac9 = frequencyCluster7[i] / len(clusterMatrix7)
            entropyCluster7 = entropyCluster7 + (-frac9 * np.log2(frac9))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster7 = (1 / 2) * entropyCluster7
        print("entrophy of cluster 7:", entropyCluster7)

        cluster8High = []
        for i in range(0, len(clusterMatrix8)):
            cluster8High.append(df.iloc[clusterMatrix8[i]][3])
        print("cluster8High-------------", cluster8High)
        counterCluster8 = collections.Counter(cluster8High)
        frequencyCluster8 = list(counterCluster8.values())
        print("frequency of cluster 8:", frequencyCluster8)
        for i in range(0, len(frequencyCluster8)):
            frac10 = frequencyCluster8[i] / len(clusterMatrix8)
            entropyCluster8 = entropyCluster8 + (-frac10 * np.log2(frac10))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster8 = (1 / 2) * entropyCluster8
        print("entrophy of cluster 8:", entropyCluster8)

        cluster9High = []
        for i in range(0, len(clusterMatrix9)):
            cluster9High.append(df.iloc[clusterMatrix9[i]][3])
        print("cluster9High-------------", cluster9High)
        counterCluster9 = collections.Counter(cluster9High)
        frequencyCluster9 = list(counterCluster9.values())
        print("frequency of cluster 9:", frequencyCluster9)
        for i in range(0, len(frequencyCluster9)):
            frac11 = frequencyCluster9[i] / len(clusterMatrix9)
            entropyCluster9 = entropyCluster9 + (-frac11 * np.log2(frac11))
            # print("entrophy of cluster 3:", entropyCluster3)
        entropyCluster9 = (1 / 2) * entropyCluster9
        print("entrophy of cluster 9:", entropyCluster9)

        mutualInformation=entropyClass-(entropyCluster1+entropyCluster2+entropyCluster3+entropyCluster4+entropyCluster5+entropyCluster6+entropyCluster7+entropyCluster8+entropyCluster9)
        NMI=(2*mutualInformation)/(entropyCluster+entropyClass)
        print("Single Link: NMI======",NMI)
        #---------------------------------NMI Value ealculation End---------------------------------------


# ****----------Single Link Function End---------------------------*****

# ****----------Complete Link Function start---------------------------*****

def completeLink(df):
            # r1 = set(df[0][2])
            # print(r1)
            w, h = len(df), len(df);
            similarMatrix = [[0 for x in range(w)] for y in range(h)]
            for i in range(0, len(df)):
                for j in range(0, len(df)):
                    similarMatrix[i][j] = 100

            for i in range(0, len(df)):
                for j in range(0, len(df)):

                    if (i < j):
                        l1 = df.iloc[i][2].split('\n')
                        l2 = df.iloc[j][2].split('\n')
                        r1 = set(l1)
                        r2 = set(l2)
                        intersection_len = len(r1.intersection(r2))
                        union_len = len(r1) + len(r2) - intersection_len
                        jaccard = intersection_len / union_len
                        if(jaccard==0.0):
                         similarMatrix[j][i]=3
                        else:
                         similarMatrix[j][i] = jaccard
                        #print("jaccard of ", i, " and ", j, " is ", jaccard)
                    if (i == j):
                        similarMatrix[i][j] = 100

            #print(similarMatrix)
            clusterMatrix1 = []
            clusterMatrix2 = []
            clusterMatrix3 = []
            clusterMatrix4 = []
            clusterMatrix5 = []
            clusterMatrix6 = []
            clusterMatrix7 = []
            clusterMatrix8 = []
            clusterMatrix9 = []

            # ....................Creating Cluster using complete Link  Start ..........................#
            clusterCount = len(df)
            while (clusterCount >= 9):
                flag = 0
                min = 3
                first = -9
                second = -9

                for i in range(0, len(df)):
                    for j in range(0, len(df)):

                        if (min > similarMatrix[i][j]):
                            flag = 1
                            min = similarMatrix[i][j]
                            first = i
                            second = j
                similarMatrix[first][second] = 100
                #print("min======",min, "first and second", first, second)
                if (clusterCount == len(df)):
                    clusterMatrix1.append(first)
                    clusterMatrix1.append(second)

                    clusterCount = clusterCount - len(clusterMatrix1) + 1
                if (flag == 1):
                    if clusterMatrix1:
                        if first not in clusterMatrix1 and second in clusterMatrix1:
                            clusterMatrix1.append(first)
                            clusterCount = clusterCount - 1

                        if second not in clusterMatrix1 and first in clusterMatrix1:
                            clusterMatrix1.append(second)
                            clusterCount = clusterCount - 1


                        if clusterMatrix1 and first not in clusterMatrix1 and second not in clusterMatrix1:
                            if not clusterMatrix2:
                                clusterMatrix2.append(first)
                                clusterMatrix2.append(second)
                                clusterCount = clusterCount - len(clusterMatrix2) + 1

                            else:
                                if first not in clusterMatrix2 and second in clusterMatrix2:
                                    clusterMatrix2.append(first)
                                    clusterCount = clusterCount - 1

                                if second not in clusterMatrix2 and first in clusterMatrix2:
                                    clusterMatrix2.append(second)
                                    clusterCount = clusterCount - 1

                            if clusterMatrix2 and first not in clusterMatrix2 and second not in clusterMatrix2:
                                if not clusterMatrix3:
                                    clusterMatrix3.append(first)
                                    clusterMatrix3.append(second)

                                    clusterCount = clusterCount - len(clusterMatrix3) + 1
                                else:
                                    if first not in clusterMatrix3 and second in clusterMatrix3:
                                        clusterMatrix3.append(first)
                                        clusterCount = clusterCount - 1

                                    if second not in clusterMatrix3 and first in clusterMatrix3:
                                        clusterMatrix3.append(second)
                                        clusterCount = clusterCount - 1

                                if clusterMatrix3 and first not in clusterMatrix3 and second not in clusterMatrix3:
                                    if not clusterMatrix4:
                                        clusterMatrix4.append(first)
                                        clusterMatrix4.append(second)
                                        clusterCount = clusterCount - len(clusterMatrix4) + 1

                                    else:
                                        if first not in clusterMatrix4 and second in clusterMatrix4:
                                            clusterMatrix4.append(first)
                                            clusterCount = clusterCount - 1

                                        if second not in clusterMatrix4 and first in clusterMatrix4:
                                            clusterMatrix4.append(second)
                                            clusterCount = clusterCount - 1

                                    if clusterMatrix4 and first not in clusterMatrix4 and second not in clusterMatrix4:
                                        if not clusterMatrix5:
                                            clusterMatrix5.append(first)
                                            clusterMatrix5.append(second)
                                            clusterCount = clusterCount - len(clusterMatrix5) + 1

                                        else:
                                            if first not in clusterMatrix5 and second in clusterMatrix5:
                                                clusterMatrix5.append(first)
                                                clusterCount = clusterCount - 1

                                            if second not in clusterMatrix5 and first in clusterMatrix5:
                                                clusterMatrix5.append(second)
                                                clusterCount = clusterCount - 1

                                        if clusterMatrix5 and first not in clusterMatrix5 and second not in clusterMatrix5:
                                            if not clusterMatrix6:
                                                clusterMatrix6.append(first)
                                                clusterMatrix6.append(second)
                                                clusterCount = clusterCount - len(clusterMatrix6) + 1

                                            else:
                                                if first not in clusterMatrix6 and second in clusterMatrix6:
                                                    clusterMatrix6.append(first)
                                                    clusterCount = clusterCount - 1

                                                if second not in clusterMatrix6 and first in clusterMatrix6:
                                                    clusterMatrix6.append(second)
                                                    clusterCount = clusterCount - 1

                                            if clusterMatrix6 and first not in clusterMatrix6 and second not in clusterMatrix6:
                                                if not clusterMatrix7:
                                                    clusterMatrix7.append(first)
                                                    clusterMatrix7.append(second)
                                                    clusterCount = clusterCount - len(clusterMatrix7) + 1

                                                else:
                                                    if first not in clusterMatrix7 and second in clusterMatrix7:
                                                        clusterMatrix7.append(first)
                                                        clusterCount = clusterCount - 1

                                                    if second not in clusterMatrix7 and first in clusterMatrix7:
                                                        clusterMatrix7.append(second)
                                                        clusterCount = clusterCount - 1

                                                if clusterMatrix7 and first not in clusterMatrix7 and second not in clusterMatrix7:
                                                    if not clusterMatrix8:
                                                        clusterMatrix8.append(first)
                                                        clusterMatrix8.append(second)
                                                        clusterCount = clusterCount - len(clusterMatrix8) + 1

                                                    else:
                                                        if first not in clusterMatrix8 and second in clusterMatrix8:
                                                            clusterMatrix8.append(first)
                                                            clusterCount = clusterCount - 1

                                                        if second not in clusterMatrix8 and first in clusterMatrix8:
                                                            clusterMatrix8.append(second)
                                                            clusterCount = clusterCount - 1

                                                    if clusterMatrix8 and first not in clusterMatrix8 and second not in clusterMatrix8:
                                                        if not clusterMatrix9:
                                                            clusterMatrix9.append(first)
                                                            clusterMatrix9.append(second)
                                                            clusterCount = clusterCount - len(clusterMatrix9) + 1

                                                        else:
                                                            if first not in clusterMatrix9 and second in clusterMatrix9:
                                                                clusterMatrix9.append(first)
                                                                clusterCount = clusterCount - 1

                                                            if second not in clusterMatrix9 and first in clusterMatrix9:
                                                                clusterMatrix9.append(second)
                                                                clusterCount = clusterCount - 1


                #print(clusterMatrix1[1])
                #print(similarMatrix[30][1])
                """for i in range (0,len(df)):
                    minimum=100
                    for j in range (0,len(clusterMatrix1)):
                        #print("j====",j)
                        if (similarMatrix[clusterMatrix1[j]][i]<minimum):
                            minimum=similarMatrix[clusterMatrix1[j]][i]
                    for k in range (0,len(clusterMatrix1)):
                         similarMatrix[clusterMatrix1[k]][i]=minimum"""




            #print("complete Link cluster 1 ===", clusterMatrix1)
            for i in range (0,len(df)):
                if i not in clusterMatrix1:
                    clusterMatrix2.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2 :
                    clusterMatrix3.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 :
                    clusterMatrix4.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 and i not in clusterMatrix4 :
                    clusterMatrix5.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 and i not in clusterMatrix4 and i not in clusterMatrix5 :
                    clusterMatrix6.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 and i not in clusterMatrix4 and i not in clusterMatrix5 and i not in clusterMatrix6:
                    clusterMatrix7.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 and i not in clusterMatrix4 and i not in clusterMatrix5 and i not in clusterMatrix6 and i not in clusterMatrix7:
                    clusterMatrix8.append(i)
                    break;
            for i in range (0,len(df)):
                if i not in clusterMatrix1 and i not in clusterMatrix2  and i not in clusterMatrix3 and i not in clusterMatrix4 and i not in clusterMatrix5 and i not in clusterMatrix6 and i not in clusterMatrix7 and i not in clusterMatrix8:
                    clusterMatrix9.append(i)
                    break;
            print("complete Link cluster 2==", clusterMatrix2)
            print("complete Link cluster 3==", clusterMatrix3)
            print("complete Link cluster 4==", clusterMatrix4)
            print("complete Link cluster 5===", clusterMatrix5)
            print("complete Link cluster 6==", clusterMatrix6)
            print("complete Link cluster 7==", clusterMatrix7)
            print("complete Link cluster 8==", clusterMatrix8)
            print("complete Link cluster 9==", clusterMatrix9)

            print("single Link cluster 1 length ===", len(clusterMatrix1))
            print("single Link cluster 2 length==", len(clusterMatrix2))
            print("single Link cluster 3 length==", len(clusterMatrix3))
            print("single Link cluster 4 length==", len(clusterMatrix4))
            print("single Link cluster 5 length===", len(clusterMatrix5))
            print("single Link cluster 6 length==", len(clusterMatrix6))
            print("single Link cluster 7 length==", len(clusterMatrix7))
            print("single Link cluster 8 length==", len(clusterMatrix8))
            print("single Link cluster 9 length==", len(clusterMatrix9))

            ###NMI VALUE CalCulation.......................................

            countElementsCluster = []
            countElementsCluster.append(len(clusterMatrix1))
            countElementsCluster.append(len(clusterMatrix2))
            countElementsCluster.append(len(clusterMatrix3))
            countElementsCluster.append(len(clusterMatrix4))
            countElementsCluster.append(len(clusterMatrix5))
            countElementsCluster.append(len(clusterMatrix6))
            countElementsCluster.append(len(clusterMatrix7))
            countElementsCluster.append(len(clusterMatrix8))
            countElementsCluster.append(len(clusterMatrix9))

            highLevelDomain = []
            for i in range(0, len(df)):
                highLevelDomain.append(df.iloc[i][3])

            print(len(highLevelDomain))

            counter = collections.Counter(highLevelDomain)
            frequency = list(counter.values())
            uniquehighLevelDomain = list(set(highLevelDomain))
            print(uniquehighLevelDomain)
            print(frequency)
            entropyClass = 0
            entropyCluster = 0
            entropyCluster1 = 0
            entropyCluster2 = 0
            entropyCluster3 = 0
            entropyCluster4 = 0
            entropyCluster5 = 0
            entropyCluster6 = 0
            entropyCluster7 = 0
            entropyCluster8 = 0
            entropyCluster9 = 0
            for i in range(0, len(frequency)):
                frac1 = frequency[i] / 150

                entropyClass = entropyClass + (-frac1 * np.log2(frac1))
            print("entrophy of Class:", entropyClass)
            for i in range(0, 9):
                frac2 = countElementsCluster[i] / 150
                if (frac2 == 0):
                    entropyCluster += 0
                else:
                    entropyCluster = entropyCluster + (-frac2 * np.log2(frac2))
            print("entrophy of cluster:", entropyCluster)

            cluster1High = []
            for i in range(0, len(clusterMatrix1)):
                cluster1High.append(df.iloc[clusterMatrix1[i]][3])
            print("cluster1High-------------", cluster1High)
            counterCluster1 = collections.Counter(cluster1High)
            frequencyCluster1 = list(counterCluster1.values())
            for i in range(0, len(frequencyCluster1)):
                frac3 = frequencyCluster1[i] / len(clusterMatrix1)
                entropyCluster1 = entropyCluster1 + (-frac3 * np.log2(frac3))
            entropyCluster1 = (1 / 2) * entropyCluster1
            print("entrophy of cluster 1:", entropyCluster1)

            cluster2High = []
            for i in range(0, len(clusterMatrix2)):
                cluster2High.append(df.iloc[clusterMatrix2[i]][3])
            print("cluster2High-------------", cluster2High)
            counterCluster2 = collections.Counter(cluster2High)
            frequencyCluster2 = list(counterCluster2.values())
            print("frequency of cluster 2:", frequencyCluster2)
            for i in range(0, len(frequencyCluster2)):
                frac4 = frequencyCluster2[i] / len(clusterMatrix2)
                entropyCluster2 = entropyCluster2 + (-frac4 * np.log2(frac4))
                # print("entrophy of cluster 2:", entropyCluster2)
            entropyCluster2 = (1 / 2) * entropyCluster2
            print("entrophy of cluster 2:", entropyCluster2)

            cluster3High = []
            for i in range(0, len(clusterMatrix3)):
                cluster3High.append(df.iloc[clusterMatrix3[i]][3])
            print("cluster3High-------------", cluster3High)
            counterCluster3 = collections.Counter(cluster3High)
            frequencyCluster3 = list(counterCluster3.values())
            print("frequency of cluster 3:", frequencyCluster3)
            for i in range(0, len(frequencyCluster3)):
                frac5 = frequencyCluster3[i] / len(clusterMatrix3)
                entropyCluster3 = entropyCluster3 + (-frac5 * np.log2(frac5))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster3 = (1 / 2) * entropyCluster3
            print("entrophy of cluster 3:", entropyCluster3)

            cluster4High = []
            for i in range(0, len(clusterMatrix4)):
                cluster4High.append(df.iloc[clusterMatrix4[i]][3])
            print("cluster4High-------------", cluster4High)
            counterCluster4 = collections.Counter(cluster4High)
            frequencyCluster4 = list(counterCluster4.values())
            print("frequency of cluster 4:", frequencyCluster4)
            for i in range(0, len(frequencyCluster4)):
                frac6 = frequencyCluster4[i] / len(clusterMatrix4)
                entropyCluster4 = entropyCluster4 + (-frac6 * np.log2(frac6))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster4 = (1 / 2) * entropyCluster4
            print("entrophy of cluster 4:", entropyCluster4)

            cluster5High = []
            for i in range(0, len(clusterMatrix5)):
                cluster5High.append(df.iloc[clusterMatrix5[i]][3])
            print("cluster5High-------------", cluster5High)
            counterCluster5 = collections.Counter(cluster5High)
            frequencyCluster5 = list(counterCluster5.values())
            print("frequency of cluster 5:", frequencyCluster5)
            for i in range(0, len(frequencyCluster5)):
                frac7 = frequencyCluster5[i] / len(clusterMatrix5)
                entropyCluster5 = entropyCluster5 + (-frac7 * np.log2(frac7))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster5 = (1 / 2) * entropyCluster5
            print("entrophy of cluster 5:", entropyCluster5)

            cluster6High = []
            for i in range(0, len(clusterMatrix6)):
                cluster6High.append(df.iloc[clusterMatrix6[i]][3])
            print("cluster5High-------------", cluster6High)
            counterCluster6 = collections.Counter(cluster6High)
            frequencyCluster6 = list(counterCluster6.values())
            print("frequency of cluster 6:", frequencyCluster6)
            for i in range(0, len(frequencyCluster6)):
                frac8 = frequencyCluster6[i] / len(clusterMatrix6)
                entropyCluster6 = entropyCluster6 + (-frac8 * np.log2(frac8))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster6 = (1 / 2) * entropyCluster6
            print("entrophy of cluster 6:", entropyCluster6)

            cluster7High = []
            for i in range(0, len(clusterMatrix7)):
                cluster7High.append(df.iloc[clusterMatrix7[i]][3])
            print("cluster5High-------------", cluster7High)
            counterCluster7 = collections.Counter(cluster7High)
            frequencyCluster7 = list(counterCluster7.values())
            print("frequency of cluster 7:", frequencyCluster7)
            for i in range(0, len(frequencyCluster7)):
                frac9 = frequencyCluster7[i] / len(clusterMatrix7)
                entropyCluster7 = entropyCluster7 + (-frac9 * np.log2(frac9))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster7 = (1 / 2) * entropyCluster7
            print("entrophy of cluster 7:", entropyCluster7)

            cluster8High = []
            for i in range(0, len(clusterMatrix8)):
                cluster8High.append(df.iloc[clusterMatrix8[i]][3])
            print("cluster8High-------------", cluster8High)
            counterCluster8 = collections.Counter(cluster8High)
            frequencyCluster8 = list(counterCluster8.values())
            print("frequency of cluster 8:", frequencyCluster8)
            for i in range(0, len(frequencyCluster8)):
                frac10 = frequencyCluster8[i] / len(clusterMatrix8)
                entropyCluster8 = entropyCluster8 + (-frac10 * np.log2(frac10))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster8 = (1 / 2) * entropyCluster8
            print("entrophy of cluster 8:", entropyCluster8)

            """cluster9High = []
            for i in range(0, len(clusterMatrix9)):
                cluster9High.append(df.iloc[clusterMatrix9[i]][3])
            print("cluster9High-------------", cluster9High)
            counterCluster9 = collections.Counter(cluster9High)
            frequencyCluster9 = list(counterCluster9.values())
            print("frequency of cluster 9:", frequencyCluster9)
            for i in range(0, len(frequencyCluster9)):
                frac11 = frequencyCluster9[i] / len(clusterMatrix9)
                entropyCluster9 = entropyCluster9 + (-frac11 * np.log2(frac11))
                # print("entrophy of cluster 3:", entropyCluster3)
            entropyCluster9 = (1 / 2) * entropyCluster9
            print("entrophy of cluster 9:", entropyCluster9)"""

            mutualInformation = entropyClass - (
                        entropyCluster1 + entropyCluster2 + entropyCluster3 + entropyCluster4 + entropyCluster5 + entropyCluster6 + entropyCluster7 + entropyCluster8 )
            NMI = (2 * mutualInformation) / (entropyCluster + entropyClass)
            print("Complete Link: NMI======", NMI)
            # ---------------------------------NMI Value ealculation End---------------------------------------









        # ....................Creating Cluster using Complete Link  End ..........................#

# ****----------Complete Link Function End---------------------------*****


def Girvan_newman():
    G = nx.Graph()

    df = pd.read_csv("AAAI.csv")

    thersold = 0.2
    w, h = len(df), len(df);
    similarMatrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(0, len(df)):
        for j in range(0, len(df)):
            similarMatrix[i][j] = -1

    for i in range(0, len(df)):
        for j in range(0, len(df)):

            if (i < j):
                l1 = df.iloc[i][2].split('\n')
                l2 = df.iloc[j][2].split('\n')
                r1 = set(l1)
                r2 = set(l2)
                intersection_len = len(r1.intersection(r2))
                union_len = len(r1) + len(r2) - intersection_len
                jaccard = intersection_len / union_len
                similarMatrix[j][i] = jaccard
                if (jaccard > thersold):
                    # print('zzzzzzzzzzzzz',z)

                    #print('i', i, 'j', j)
                    G.add_edges_from([(i, j)], weight=thersold)
                #print("jaccard of ", i, " and ", j, " is ", jaccard)
            if (i == j):
                similarMatrix[i][j] = -1

    print(similarMatrix)
    print(nx.info(G))
    nx.draw(G)
    #plt.show()
    cc = list(nx.connected_component_subgraphs(G))

    length_of_connected_component = len(cc)
    while (length_of_connected_component <= 8):
        centrelity = nx.edge_betweenness_centrality(G)
        list_centrelity = list(centrelity.items())
        list_centrelity.sort(key=lambda x: x[1], reverse=True)
        edge_remove = list_centrelity[0][0]
        G.remove_edge(*edge_remove)
        ccc = list(nx.connected_component_subgraphs(G))

        length_of_connected_component = len(ccc)
        # print("hsjhsjsh",list_centrelity)
       # print("edge to remove", edge_remove)

    nx.draw(G)
    #plt.show()
    cccc = nx.connected_component_subgraphs(G)
    clusterMatrix1 = []
    clusterMatrix2 = []
    clusterMatrix3 = []
    clusterMatrix4 = []
    clusterMatrix5 = []
    clusterMatrix6 = []
    clusterMatrix7 = []
    clusterMatrix8 = []
    clusterMatrix9 = []
    count = 1
    for i in cccc:
        if (count == 1):
            clusterMatrix1 = list(i.nodes())

        if (count == 2):
            clusterMatrix2 = list(i.nodes())

        if (count == 3):
            clusterMatrix3 = list(i.nodes())

        if (count == 4):
            clusterMatrix4 = list(i.nodes())

        if (count == 5):
            clusterMatrix5 = list(i.nodes())

        if (count == 6):
            clusterMatrix6 = list(i.nodes())

        if (count == 7):
            clusterMatrix7 = list(i.nodes())

        if (count == 8):
            clusterMatrix8 = list(i.nodes())

        if (count == 9):
            clusterMatrix9 = list(i.nodes())
        count = count + 1

    print("Girvan-Newman cluster1: ", clusterMatrix1)
    print("Girvan-Newman cluster2: ", clusterMatrix2)
    print("Girvan-Newman cluster3: ", clusterMatrix3)
    print("Girvan-Newman cluster4: ", clusterMatrix4)
    print("Girvan-Newman cluster5: ", clusterMatrix5)
    print("Girvan-Newman cluster6: ", clusterMatrix6)
    print("Girvan-Newman cluster7: ", clusterMatrix7)
    print("Girvan-Newman cluster8: ", clusterMatrix8)
    print("Girvan-Newman cluster9: ", clusterMatrix9)

    print("Girvan-Newman cluster1 length: ", len(clusterMatrix1))
    print("Girvan-Newman cluster2 length: ", len(clusterMatrix2))
    print("Girvan-Newman cluster3 length: ", len(clusterMatrix3))
    print("Girvan-Newman cluster4 length: ", len(clusterMatrix4))
    print("Girvan-Newman cluster5 length: ", len(clusterMatrix5))
    print("Girvan-Newman cluster6 length: ", len(clusterMatrix6))
    print("Girvan-Newman cluster7 length: ", len(clusterMatrix7))
    print("Girvan-Newman cluster8 length: ", len(clusterMatrix8))
    print("Girvan-Newman cluster9 length: ", len(clusterMatrix9))

    ###NMI VALUE CalCulation.......................................

    countElementsCluster = []
    countElementsCluster.append(len(clusterMatrix1))
    countElementsCluster.append(len(clusterMatrix2))
    countElementsCluster.append(len(clusterMatrix3))
    countElementsCluster.append(len(clusterMatrix4))
    countElementsCluster.append(len(clusterMatrix5))
    countElementsCluster.append(len(clusterMatrix6))
    countElementsCluster.append(len(clusterMatrix7))
    countElementsCluster.append(len(clusterMatrix8))
    countElementsCluster.append(len(clusterMatrix9))

    highLevelDomain = []
    for i in range(0, len(df)):
        highLevelDomain.append(df.iloc[i][3])

    print(len(highLevelDomain))

    counter = collections.Counter(highLevelDomain)
    frequency = list(counter.values())
    uniquehighLevelDomain = list(set(highLevelDomain))
    print(uniquehighLevelDomain)
    print(frequency)
    entropyClass = 0
    entropyCluster = 0
    entropyCluster1 = 0
    entropyCluster2 = 0
    entropyCluster3 = 0
    entropyCluster4 = 0
    entropyCluster5 = 0
    entropyCluster6 = 0
    entropyCluster7 = 0
    entropyCluster8 = 0
    entropyCluster9 = 0
    for i in range(0, len(frequency)):
        frac1 = frequency[i] / 150

        entropyClass = entropyClass + (-frac1 * np.log2(frac1))
    print("entrophy of Class:", entropyClass)
    for i in range(0, 9):
        frac2 = countElementsCluster[i] / 150
        if (frac2 == 0):
            entropyCluster += 0
        else:
            entropyCluster = entropyCluster + (-frac2 * np.log2(frac2))
    print("entrophy of cluster:", entropyCluster)

    cluster1High = []
    for i in range(0, len(clusterMatrix1)):
        cluster1High.append(df.iloc[clusterMatrix1[i]][3])
    print("cluster1High-------------", cluster1High)
    counterCluster1 = collections.Counter(cluster1High)
    frequencyCluster1 = list(counterCluster1.values())
    for i in range(0, len(frequencyCluster1)):
        frac3 = frequencyCluster1[i] / len(clusterMatrix1)
        entropyCluster1 = entropyCluster1 + (-frac3 * np.log2(frac3))
    entropyCluster1 = (1 / 2) * entropyCluster1
    print("entrophy of cluster 1:", entropyCluster1)

    cluster2High = []
    for i in range(0, len(clusterMatrix2)):
        cluster2High.append(df.iloc[clusterMatrix2[i]][3])
    print("cluster2High-------------", cluster2High)
    counterCluster2 = collections.Counter(cluster2High)
    frequencyCluster2 = list(counterCluster2.values())
    print("frequency of cluster 2:", frequencyCluster2)
    for i in range(0, len(frequencyCluster2)):
        frac4 = frequencyCluster2[i] / len(clusterMatrix2)
        entropyCluster2 = entropyCluster2 + (-frac4 * np.log2(frac4))
        # print("entrophy of cluster 2:", entropyCluster2)
    entropyCluster2 = (1 / 2) * entropyCluster2
    print("entrophy of cluster 2:", entropyCluster2)

    cluster3High = []
    for i in range(0, len(clusterMatrix3)):
        cluster3High.append(df.iloc[clusterMatrix3[i]][3])
    print("cluster3High-------------", cluster3High)
    counterCluster3 = collections.Counter(cluster3High)
    frequencyCluster3 = list(counterCluster3.values())
    print("frequency of cluster 3:", frequencyCluster3)
    for i in range(0, len(frequencyCluster3)):
        frac5 = frequencyCluster3[i] / len(clusterMatrix3)
        entropyCluster3 = entropyCluster3 + (-frac5 * np.log2(frac5))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster3 = (1 / 2) * entropyCluster3
    print("entrophy of cluster 3:", entropyCluster3)

    cluster4High = []
    for i in range(0, len(clusterMatrix4)):
        cluster4High.append(df.iloc[clusterMatrix4[i]][3])
    print("cluster4High-------------", cluster4High)
    counterCluster4 = collections.Counter(cluster4High)
    frequencyCluster4 = list(counterCluster4.values())
    print("frequency of cluster 4:", frequencyCluster4)
    for i in range(0, len(frequencyCluster4)):
        frac6 = frequencyCluster4[i] / len(clusterMatrix4)
        entropyCluster4 = entropyCluster4 + (-frac6 * np.log2(frac6))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster4 = (1 / 2) * entropyCluster4
    print("entrophy of cluster 4:", entropyCluster4)

    cluster5High = []
    for i in range(0, len(clusterMatrix5)):
        cluster5High.append(df.iloc[clusterMatrix5[i]][3])
    print("cluster5High-------------", cluster5High)
    counterCluster5 = collections.Counter(cluster5High)
    frequencyCluster5 = list(counterCluster5.values())
    print("frequency of cluster 5:", frequencyCluster5)
    for i in range(0, len(frequencyCluster5)):
        frac7 = frequencyCluster5[i] / len(clusterMatrix5)
        entropyCluster5 = entropyCluster5 + (-frac7 * np.log2(frac7))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster5 = (1 / 2) * entropyCluster5
    print("entrophy of cluster 5:", entropyCluster5)

    cluster6High = []
    for i in range(0, len(clusterMatrix6)):
        cluster6High.append(df.iloc[clusterMatrix6[i]][3])
    print("cluster5High-------------", cluster6High)
    counterCluster6 = collections.Counter(cluster6High)
    frequencyCluster6 = list(counterCluster6.values())
    print("frequency of cluster 6:", frequencyCluster6)
    for i in range(0, len(frequencyCluster6)):
        frac8 = frequencyCluster6[i] / len(clusterMatrix6)
        entropyCluster6 = entropyCluster6 + (-frac8 * np.log2(frac8))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster6 = (1 / 2) * entropyCluster6
    print("entrophy of cluster 6:", entropyCluster6)

    cluster7High = []
    for i in range(0, len(clusterMatrix7)):
        cluster7High.append(df.iloc[clusterMatrix7[i]][3])
    print("cluster5High-------------", cluster7High)
    counterCluster7 = collections.Counter(cluster7High)
    frequencyCluster7 = list(counterCluster7.values())
    print("frequency of cluster 7:", frequencyCluster7)
    for i in range(0, len(frequencyCluster7)):
        frac9 = frequencyCluster7[i] / len(clusterMatrix7)
        entropyCluster7 = entropyCluster7 + (-frac9 * np.log2(frac9))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster7 = (1 / 2) * entropyCluster7
    print("entrophy of cluster 7:", entropyCluster7)

    cluster8High = []
    for i in range(0, len(clusterMatrix8)):
        cluster8High.append(df.iloc[clusterMatrix8[i]][3])
    print("cluster8High-------------", cluster8High)
    counterCluster8 = collections.Counter(cluster8High)
    frequencyCluster8 = list(counterCluster8.values())
    print("frequency of cluster 8:", frequencyCluster8)
    for i in range(0, len(frequencyCluster8)):
        frac10 = frequencyCluster8[i] / len(clusterMatrix8)
        entropyCluster8 = entropyCluster8 + (-frac10 * np.log2(frac10))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster8 = (1 / 2) * entropyCluster8
    print("entrophy of cluster 8:", entropyCluster8)

    cluster9High = []
    for i in range(0, len(clusterMatrix9)):
        cluster9High.append(df.iloc[clusterMatrix9[i]][3])
    print("cluster9High-------------", cluster9High)
    counterCluster9 = collections.Counter(cluster9High)
    frequencyCluster9 = list(counterCluster9.values())
    print("frequency of cluster 9:", frequencyCluster9)
    for i in range(0, len(frequencyCluster9)):
        frac11 = frequencyCluster9[i] / len(clusterMatrix9)
        entropyCluster9 = entropyCluster9 + (-frac11 * np.log2(frac11))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster9 = (1 / 2) * entropyCluster9
    print("entrophy of cluster 9:", entropyCluster9)

    """cluster9High = []
    for i in range(0, len(clusterMatrix9)):
        cluster9High.append(df.iloc[clusterMatrix9[i]][3])
    print("cluster9High-------------", cluster9High)
    counterCluster9 = collections.Counter(cluster9High)
    frequencyCluster9 = list(counterCluster9.values())
    print("frequency of cluster 9:", frequencyCluster9)
    for i in range(0, len(frequencyCluster9)):
        frac11 = frequencyCluster9[i] / len(clusterMatrix9)
        entropyCluster9 = entropyCluster9 + (-frac11 * np.log2(frac11))
        # print("entrophy of cluster 3:", entropyCluster3)
    entropyCluster9 = (1 / 2) * entropyCluster9
    print("entrophy of cluster 9:", entropyCluster9)"""

    mutualInformation = entropyClass - (
            entropyCluster1 + entropyCluster2 + entropyCluster3 + entropyCluster4 + entropyCluster5 + entropyCluster6 + entropyCluster7 + entropyCluster8 + entropyCluster9)
    NMI = (2 * mutualInformation) / (entropyCluster + entropyClass)
    print("Girvan-Newman: NMI======", NMI)
    # ---------------------------------NMI Value ealculation End---------------------------------------


df= pd.read_csv("AAAI.csv")
singleLink(df)
completeLink(df)
Girvan_newman()













































"""highLevelDomain=[]
for i in range (0, len(df)):
   highLevelDomain.append(df.iloc[i][3])

print(len(highLevelDomain))

counter=collections.Counter(highLevelDomain)
frequency=list(counter.values())
uniquehighLevelDomain=list(set(highLevelDomain))
print(uniquehighLevelDomain)
print(frequency)
entropyClass=0
for i in range(0, len(frequency)):
    frac=frequency[i]/150
    entropyClass=entropyClass+( -frac * np.log2(frac))
print(entropyClass)"""


