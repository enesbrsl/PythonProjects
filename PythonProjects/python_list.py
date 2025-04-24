def add_lists(a, b):
    new_list=[]
    for i in range(len(a)):
        new_list.append(a[i]+b[i])
    return new_list

print(add_lists([1, 1], [1, 1]))
print(add_lists([1, 2], [1, 4]))    
print(add_lists([1, 2, 1], [1, 4, 3]))
#%%

def mult_lists(a, b):
    sonuc=0
    for i in range(len(a)):
        sonuc+=a[i]*b[i]
    return sonuc
print(mult_lists([1, 1], [1, 1]))
print(mult_lists([1, 2], [1, 4]))  
print(mult_lists([1, 2, 1], [1, 4, 3]))
#%%
def add_row(matrix):
    new_row =[0] * len(matrix[0])  
    return matrix + [new_row] 

m = [[0, 0], [0, 0]]
print(add_row(m)) 
n = [[3, 2, 5], [1, 4, 7]]
print(add_row(n)) 
print(n) 
#%%
def add_column(matrix):
    
    new_matrix = [row + [0] for row in matrix]
    return new_matrix

m = [[0, 0], [0, 0]]
print(add_column(m))  
n = [[3, 2], [5, 1], [4, 7]]
print(add_column(n)) 
print(n) 
#%%
def add_matrices(m1, m2):
    if (len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        print("matris boyutları aynı degil")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result
a = [[1, 2], [3, 4]]
b = [[2, 2], [2, 2]]
print(add_matrices(a, b)) 
c = [[8, 2], [3, 4], [5, 7]]
d = [[3, 2], [9, 2], [10, 12]]
print(add_matrices(c, d))  
print(c) 
print(d) 
#%%
def scalar_mult(n, m):
    sonuc = []
    for row in m:
        sonuc_indis= [n * element for element in row]
        sonuc.append(sonuc_indis)
    return sonuc
a = [[1, 2], [3, 4]]
print(scalar_mult(3, a))  
b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
print(scalar_mult(10, b)) 
print(b) 
#%%
def row_times_column(m1, row, m2, column):
    sonuc = 0
    for i in range(len(m1[row])):
        for j in range(len(m2)):
            if (i == j):  
                sonuc += m1[row][i] * m2[j][column]
    return sonuc


print(row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)) 
print(row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)) 
print(row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)) 
print(row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)) 
#%%
def matrix_mult(m1, m2):
    sonuc = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            element = 0
            for k in range(len(m1[i])):
                element += m1[i][k] * m2[k][j]
            row.append(element)
        sonuc.append(row)
    return sonuc
print(matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]])) 
print(matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1], [2, 3]]))
print(matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])) 
 

 



   
    
    
    
    
    
    
    
    
    
    
    
    
    