import numpy as np
import csv
import random

class Data:
    def __init__(self, feature, clustering):
        self.feature = feature
        self.clustering = clustering



def clusterCenter(data, degree):
    feature = [datas.feature for datas in data]

    center = []
    for i in range (len(feature[0])):
        center.append([])
        for j in range (W):
            temp1 = 0
            temp2 = 0
            for k in range(len(data)):
                temp1 += degree[k, j] ** W
                temp2 += temp1 * feature[k][i]
            center[i].append(temp2/temp1)
    return center


def euclidianDistance(data, V):
    feature = [datas.feature for datas in data]
    distance = []
    for i in range (len(data)):
        distance.append([])
        for j in range (W):
            temp = 0
            for k in range (len(feature[0])):
                # print(feature[i][k])
                # print(center[k][j])
                temp += (feature[i][k] - V[k][j]) ** 2

            distance[i].append(temp)
            # print("\n")
    return distance


def fungsiObjective(data, degree, distance):
    temp = 0
    for i in range (len(data)):
        for j in range (W):
            temp += degree[i,j] ** W * distance[i][j] ** 2
    return temp

def perbaikiMatriks(data, distance):
    matriks = []
    for i in range(len(data)):
        matriks.append([])
        for j in range(W):
            temp = 0
            for k in range(W):
                temp += ((distance[i][j] / distance[i][k]) ** (2 / (W -1 )))
            temp = temp ** -1
            matriks[i].append(temp)

    return np.array(matriks)

def normalize (data):
    temp = []
    for i in range (len(data)):
        temp.append((data[i]-min(data))/(max(data) - min(data)))
    return temp


def find_index(arr, value):
    for i in range(len(data)):
        for j in range(len(data)):
            if arr[i][j] == value:
                return [i, j]

    return -1

data = []

with open('dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    reader = csv.reader(f, delimiter=';', quoting = csv.QUOTE_NONNUMERIC)

    for row in reader:
        data.append(Data(row[1:-1], 1))


for i in range (5):
    x = normalize([datas.feature[i] for datas in data])
    for j in range(len(data)):
        data[j].feature[i] = x[j]


C = 3
W = 3
Err = 0.00001


degree = np.zeros((len(data),C))
[m, n] = np.shape(degree)

for i in range (m):
    for j in range (n):
        degree[i,j] = random.uniform(0,1)

delta = 10000

fold = 0
count = 1

while (delta > Err):
    center = clusterCenter(data, degree)
    euclid = euclidianDistance(data, center)
    pn = fungsiObjective(data, degree, euclid)
    degree = perbaikiMatriks(data, euclid)
    for i in range(len(degree)):
        temp = []
        for j in range(C):
            temp.append(degree[i][j])
        data[i].clustering = temp.index(max(temp)) + 1

    fnew = pn

    delta = abs(fnew - fold)
    fold = fnew
    count += 1


object = [datas.clustering for datas in data]
print(object)

print(count)