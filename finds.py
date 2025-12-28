import csv
x = []
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)   # skip header

    for row in reader:
        x.append(row)
y = [0,0,1]
# 0 indicate yes and 1 incdicate no
h = None
for i in range(len(x)):
    if y[i] == 0:
        if h is None:
            h = list(x[i])
        else:
            for j in range(len(x[i])):
                if h[j] != x[i][j]:
                    h[j] = '?'

print("Final Hypothesis = ",h)
