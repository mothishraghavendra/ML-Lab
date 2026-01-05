import pandas as pd;
import math
import numpy as np;
def entropy(p,n):
    if p==0 or n==0:
        return 0
    total = p+n 
    pr = p/total
    nr = n/total
    return -(pr*math.log2(pr)+nr*math.log2(nr))

def entropy_attr(data,attr):
    seen = set(attr)
    dist = list(seen)
    total = len(attr)
    weighted_entropy = 0
    for i in dist:
        p = n = count =0 
        for j in range(len(attr)):
            if attr[j] == i: 
                count += 1
                if data[j][-1] == 'Yes':
                    p+=1
                else:
                    n+=1
        ent = entropy(p,n)
        weighted_entropy += ( count / total) * ent
    return weighted_entropy


attr = pd.read_csv("car.csv")
attr_names = attr.columns.tolist()

print("Attributes =", attr_names)
df = pd.read_csv("car.csv",header=None)
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
Ig = []
for i in range(len(trans) - 1):  
    ig = entropy_r - entropy_attr(data, trans[i])
    Ig.append(ig)


best_attr_index = Ig.index(max(Ig))
root_attr = best_attr_index

values = set(trans[root_attr])

print("\nDecision Tree (Level 1):")
print(attr_names[root_attr])

for v in values:
    p = n = 0
    for row in data:
        if row[root_attr] == v:
            if row[-1] == 'Yes':
                p += 1
            else:
                n += 1

    if p == 0:
        decision = "No"
    elif n == 0:
        decision = "Yes"
    else:
        decision = "Mixed"

    print(f" ├── {v} → {decision}")

print("\nBest attribute to split on:", attr_names[best_attr_index])


