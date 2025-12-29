import pandas as pd;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.model_selection import train_test_split;

import mathplotlib.pyplot as plt;

df = pd.read_csv("playtennis.csv",header=None)
data = df.values.tolist()
data.pop(0)



