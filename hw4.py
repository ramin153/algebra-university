import sys
import random

import pandas as pd
import math

import numpy as np
import matplotlib.pyplot as plt

class K_mean:

    def __init__(self,df,size = 2,iteration = 10):
        self.df = df
        self.size = size
        self.iteration = iteration

    def __random_centers(self):
        centers = []
        for i in range(self.size):
            center = []
            for i in self.df.columns:
                rand = round((( random.random() * (self.df[i].max()- self.df[i].min()) )+ self.df[i].min()),2)
                center.append(rand)


            centers.append(center)
        return centers

    def __mean_cluster(self,list):
        arr = np.array(list)
        return  np.mean(arr, axis=0)

    def k_mean_euclidean_distance(self):

        best_var = sys.maxsize
        best_cluster = []
        for i in range(self.iteration):

            clusters,mean = self.__k_mean(self.__euclidean_distance,True)
            new_var = 0
            for i in range(self.size):
                for j in clusters[i]:
                    new_var += self.__Variance(mean[i],j)
            if new_var < best_var:
                best_var,best_cluster = new_var,clusters
        return best_cluster,self.__find_d(best_cluster)

    def __find_d(self,clusters):
        smallest = sys.maxsize

        for i in clusters[0]:
            for j in clusters[1]:
                dist = self.__euclidean_distance(i,j)
                if (dist < smallest):
                    smallest = dist

        return smallest




    def k_mean_cos_sim(self):
        best_var = sys.maxsize
        best_cluster = []
        for i in range(self.iteration):
            clusters,mean = self.__k_mean(self.__cos_sim,False)

            new_var = 0
            for i in range(self.size):
                for j in clusters[i]:
                    new_var += self.__Variance(mean[i], j)
            if new_var < best_var:
                best_var, best_cluster = new_var, clusters
        return best_cluster,self.__find_s(best_cluster)

    def __find_s(self, clusters):
        biggest =  -sys.maxsize - 1

        for i in clusters[0]:
            for j in clusters[1]:
                dist = self.__cos_sim(i, j)
                if (dist > biggest):
                    biggest = dist

        return biggest



    def __k_mean(self,function,smaller:bool):
        cluster = self.__random_centers()
        cluster_item = []
        while True:
            cluster_item = [[] for i in range(self.size)]

            for i in range(0,len(df)):
                bestDis = 0
                if smaller:
                    bestDis = sys.maxsize
                else:
                    bestDis = -sys.maxsize - 1

                index = -1

                for j in range(len(cluster_item)):
                    distance = function(df.iloc[i],cluster[j])
                    if((smaller and bestDis > distance) or ( (not smaller) and bestDis < distance)):
                        bestDis = distance
                        index = j
                cluster_item[index].append(df.iloc[i])

            new_clusters =[]
            is_same = True


            for i in range(self.size):
                if len(cluster_item[i]) > 0:
                    new_cluster = self.__mean_cluster(cluster_item[i])
                else:
                    new_cluster = cluster[i]
                new_clusters.append(new_cluster)

                if not np.array_equal(cluster[i], new_cluster):
                    is_same = False

            if is_same :
                break
            cluster = new_clusters
        return cluster_item,cluster


    def __cos_sim(self,item1,item2):
        return np.dot(item1, item2) / (np.linalg.norm(item1) * np.linalg.norm(item2))

    def __euclidean_distance(self,item1,item2):
        return np.linalg.norm(item1-item2)

    def __Variance(self,a,b):
        result = 0

        for i in range(len(a)):
            result += (a[i] - b[i]) ** 2

        return result/len(a)




if  __name__ == "__main__":
    df = pd.read_csv('dataset.csv')
    df_np = df.to_numpy()


    k_mean = K_mean(df)

    cluster,d = k_mean.k_mean_euclidean_distance()

    which_is_zero = -1

    arr0 = np.array(cluster[0])
    arr1 = np.array(cluster[1])

    file_line = []


    if np.isin(df_np[0],arr0).all():
        which_is_zero = 0
    elif  np.isin(df_np[0],arr1).all():
        which_is_zero = 1
    else:
        raise Exception('some thing goes wrong')

    file_line.append("euclidean_distance")
    for i in df_np:
        select = -1
        if np.isin(i,arr0).all():
            select = 0
        elif np.isin(i,arr1).all():
            select = 1
        else:
            raise Exception('some thing goes wrong')

        if select == which_is_zero:
            file_line.append(f'0 {i}')
        else:
            file_line.append(f'1 {i}')

    file_line.append(f'd {d}')
    file_line.append("====================================")

    cluster,s = k_mean.k_mean_cos_sim()

    which_is_zero = -1

    arr0 = np.array(cluster[0])
    arr1 = np.array(cluster[1])
    if np.isin(df_np[0], arr0).all():
        which_is_zero = 0
    elif np.isin(df_np[0], arr1).all():
        which_is_zero = 1
    else:
        raise Exception('some thing goes wrong')

    file_line.append("cos_sim")
    for i in df_np:
        select = -1
        if np.isin(i, arr0).all():
            select = 0
        elif np.isin(i, arr1).all():
            select = 1
        else:
            raise Exception('some thing goes wrong')

        if select == which_is_zero:
            file_line.append(f'0 {i}')
        else:
            file_line.append(f'1 {i}')

    file_line.append(f's {s}')
    file_line.append("====================================")

    file = open('result.txt', 'w')

    file.write('\n'.join(file_line))

    file.close()
