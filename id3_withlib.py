import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")   

data = df.values.tolist()

attr = [row[:-1] for row in data]
lab  = [row[-1] for row in data]

x_train, x_test, y_train, y_test = train_test_split(
    attr, lab, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

print("Accuracy score =", accuracy_score(y_test, y_predict))

plt.figure(figsize=(14, 18))
plot_tree(model, filled=True)
plt.show()