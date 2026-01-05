import pandas as pd

df = pd.read_csv("car.csv")

def candidate_elimination_multiclass(df, positive_class):
    attributes = df.columns[:-1]  
    target = df.columns[-1]       

    
    S = ['0'] * len(attributes)   
    G = ['?'] * len(attributes)   
    S = [S]  
    G = [G]

    for index, row in df.iterrows():
        x = list(row[attributes])
        y = row[target]

        if y == positive_class:  
            for i in range(len(S)):
                for j in range(len(attributes)):
                    if S[i][j] == '0':  
                        S[i][j] = x[j]
                    elif S[i][j] != x[j]:
                        S[i][j] = '?'  
            G = [g for g in G if all(g[j] == '?' or g[j] == S[0][j] for j in range(len(attributes)))]
        else:  
            new_G = []
            for g in G:
                for j in range(len(attributes)):
                    if g[j] == '?' and S[0][j] != x[j]:
                        h = g.copy()
                        h[j] = S[0][j]
                        if h not in new_G:
                            new_G.append(h)
                    elif g[j] != '?' and g[j] != x[j]:
                        new_G.append(g)
            G = new_G

    return S, G

classes = df[df.columns[-1]].unique()

for cls in classes:
    S_final, G_final = candidate_elimination_multiclass(df, cls)
    print(f"\nClass: {cls}")
    print("Most Specific Hypothesis (S):", S_final)
    print("Most General Hypotheses (G):", G_final)
