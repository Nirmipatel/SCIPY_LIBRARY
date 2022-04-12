import numpy as np
from scipy.sparse import csr_matrix

# create a 2-D representation of the matrix
A = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 1],
 [0, 0, 0, 2, 0, 0]])
#for converting csr to csc represeantation:
'''print(csr_matrix(A).tocsc())
B=csr_matrix(A).todense()
print(B)'''
'''#for eliminating zero-element
mat=csr_matrix(A)
mat.eliminate_zeros()
print(mat)'''

#printing count of non-zero element
'''print('non-zero element is :',csr_matrix(A).count_nonzero())
print("Dense matrix representation: \n", A)'''
print(csr_matrix(A))
#print('non-zero data is :',csr_matrix(A).data)

'''# convert to sparse matrix representation 
S = csr_matrix(A)
print("Sparse matrix: \n",S)

# convert back to 2-D representation of the matrix
B = S.todense()
print("Dense matrix: \n", B)'''