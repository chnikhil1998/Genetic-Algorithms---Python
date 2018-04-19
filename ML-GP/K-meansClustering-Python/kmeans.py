import random
import math

def equal (C_avg_new,C_avg):
    N = 3 
    F = 4
    counter = True
    for i in range(N):
        for j in range(F):
            if C_avg_new[i][j] != C_avg[i][j]:
                counter = False
    return counter
# Cluster function

def cluster(X,C,C_avg,counter) :
    

    N = 3 
    M = 150
    F = 4
    dist = [0]*N
    d = 0
    # Initialising three clusters and a counter
    C = [[0],[0],[0]] * N
    for i in  range(M) :
        for j in range(N):
            for k in range(F):
                d+= math.pow(X[i][k]-C_avg[j][k],2)
            dist[j] = math.sqrt(d)
        C[dist.index(min(dist))].append(i)


    C_avg_new = [0] * N
    for i in range(N):
        C_avg_new[i] = [0] * F


    for i in range(N):
        for j in C[i][1:] :
            for k in range(F):
                C_avg_new[i][k] += X[j][k] / F

    return(C,C_avg_new,equal(C_avg_new,C_avg))
    

    		















# Loading the data into 2-D array A , where each row is a traning example and column is an attribute
X =  open("iris.data.txt").read().split()

for i in range(len(X)) :
    X[i] = map(float, X[i].split(","))

 # N = Number of clusters , M = Total number of training dataset

N = 3 
M = 150

# Initialising three clusters and a counter
C = [0] * N

# Initialising first cluster average
C_avg = [0] * N
for i in range(N) :
    C[i] =   random.randint(1,150)
    C_avg[i] = X[C[i]]
print C_avg
counter = True


C,C_avg,counter = cluster(X,C,C_avg,counter)
while counter == False :
    C,C_avg,counter = cluster(X,C,C_avg,counter)

