import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



def Girvan_newman():
        G = nx.Graph()





        df= pd.read_csv("AAAI.csv")


        thersold=0.2
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
                    if (jaccard > thersold):
                        # print('zzzzzzzzzzzzz',z)

                        #print('i', i, 'j', j)
                        G.add_edges_from([(i, j)], weight=thersold)
                    #print("jaccard of ",i ," and ",j, " is ", jaccard)
                if(i==j):
                    similarMatrix[i][j] = -1

        print(similarMatrix)
        print(nx.info(G))
        nx.draw(G)
        plt.show()
        cc=list(nx.connected_component_subgraphs(G))

        length_of_connected_component=len(cc)
        while(length_of_connected_component<=8):
            centrelity=nx.edge_betweenness_centrality(G)
            list_centrelity=list(centrelity.items())
            list_centrelity.sort(key=lambda x:x[1], reverse=True)
            edge_remove=list_centrelity[0][0]
            G.remove_edge(*edge_remove)
            ccc = list(nx.connected_component_subgraphs(G))

            length_of_connected_component = len(ccc)
            #print("hsjhsjsh",list_centrelity)
            print("edge to remove",edge_remove)


        nx.draw(G)
        plt.plot(label='Girvan-Newman Graph Before Cluster')
        plt.legend()
        plt.show()
        cccc=nx.connected_component_subgraphs(G)
        clusterMatrix1=[]
        clusterMatrix2=[]
        clusterMatrix3=[]
        clusterMatrix4=[]
        clusterMatrix5=[]
        clusterMatrix6=[]
        clusterMatrix7=[]
        clusterMatrix8=[]
        clusterMatrix9=[]
        count=1
        for i in cccc:
            if(count==1):
               clusterMatrix1=i.nodes()

            if (count == 2):
                clusterMatrix2 = i.nodes()

            if (count == 3):
                clusterMatrix3 = i.nodes()

            if (count == 4):
                clusterMatrix4 = i.nodes()

            if (count == 5):
                clusterMatrix5 = i.nodes()

            if (count == 6):
                clusterMatrix6 = i.nodes()

            if (count == 7):
                clusterMatrix7 = i.nodes()

            if (count == 8):
                clusterMatrix8 = i.nodes()

            if (count == 9):
                clusterMatrix9 = i.nodes()
            count=count+1



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


Girvan_newman()