import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.minimum_spanning_tree.html

# Euclidean distance
def dist(p1, p2):
    return np.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

# liste of points
dico = {
    1:(0, 0, 0),
    2:(0, -1, 0),
    3:(0, 1, 1),
    4:(5, 1, 1),
    5:(6, 0, 1),
    6:(6, 1, 1)
}

# upper triangular matrix containing the distance between each point
mat = {i:[dist(dico[i], p2) for p2 in list(dico.values())] for i in list(dico)}
df = pd.DataFrame(mat)
df.values[np.tril_indices_from(df, 0)] = 0
df.index = list(dico)
print('Distance matrix between each couple of points')
print(df)

# conversion into sparse matrix and scipy csgraph MST algo
X = csr_matrix(np.array(df))
Tcsr = minimum_spanning_tree(X)

# result into df
res = pd.DataFrame(Tcsr.toarray().astype(float))
res.columns = list(dico)
res.index = list(dico)
print('\nMST matrix')
print(res)

# Display of each couple of points
list_cpl = []
for row in list(res.index):
    for col in list(res):
        if res.loc[row][col] != 0:
            list_cpl.append((row, col))
            
print('\nOptimal couples')
print(list_cpl)
