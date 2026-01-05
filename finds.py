import csv
x = []
with open("car.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)   

    for row in reader:
        x.append(row)

attrib = [row[:-1] for row in x]
y = [row[-1] for row in x]

h = None
for i in range(len(attrib)):
    if y[i] == 'Yes':
        if h is None:
            h = list(attrib[i])
        else:
            for j in range(len(attrib[i])):
                if h[j] != attrib[i][j]:
                    h[j] = '?'

print("Final Hypothesis = ",h)
