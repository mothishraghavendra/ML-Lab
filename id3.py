import pandas as pd;
import math
import numpy as np;
def entropy(p,n):
    total = p+n 
    pr = p/total
    nr = n/total
    return -(pr*math.log2(pr)+nr*math.log2(nr))

df = pd.read_csv("playtennis.csv",header=None)
data = df.values.tolist()
data.pop(0)

trans = np.array(data).T.tolist();
dist = []
for i in range(len(trans)):
    hr = set(trans[i])
    dist.append(list(hr))

p_root = trans[-1].count(dist[-1][0])
n_root = trans[-1].count(dist[-1][1])
entropy_r = entropy(p_root,n_root)
print(entropy_r)

attr_p = []
attr_n = []

for i in range(len(dist[0])):
    p_root = trans[i].count(dist[i][0])

print(p_root) 

