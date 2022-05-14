import numpy as np
import pandas as pd



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

            print(similarMatrix)
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




            print("complete Link cluster 1 ===", clusterMatrix1)
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

            print("Complete Link cluster 1 length ===", len(clusterMatrix1))
            print("Complete Link cluster 2 length==", len(clusterMatrix2))
            print("Complete Link cluster 3 length==", len(clusterMatrix3))
            print("Complete Link cluster 4 length==", len(clusterMatrix4))
            print("Complete Link cluster 5 length===", len(clusterMatrix5))
            print("Complete Link cluster 6 length==", len(clusterMatrix6))
            print("Complete Link cluster 7 length==", len(clusterMatrix7))
            print("Complete Link cluster 8 length==", len(clusterMatrix8))
            print("Complete Link cluster 9 length==", len(clusterMatrix9))










        # ....................Creating Cluster using Complete Link  End ..........................#

# ****----------Complete Link Function End---------------------------*****





df= pd.read_csv("AAAI.csv")
singleLink(df)
completeLink(df)