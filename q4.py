import sys
from pandas import *
'''
M-> our matrix order to multiplication and vale is theirs size
chain-> our array to save multiplication results
help_chain-> help to track back
n ← M.length − 1
for i ← 1 to n
    chain[i, i] ← 0
for size ← 2 to n
    ; size is length of chain
    for i ← 1 to n − size + 1
        j ← i + size −1
        chain[i, j] ← maxValue
        ; we put maxValue to sure the value would change
        for k ← i to j − 1
            min ← chain[i, k] + chain[k+1, j] + M[i-1]*M[k]*M[j]
            if min < chain[i, j]
                chain[i, j] ← min
                help_chain[i, j] ← k
return chain and help_chain

ما دو مارتیس کمکی  استفاده می کنیم که به جواب برسیم یکی برای مسیر و یکی برای برای یافتن جواب(یا یک اریه 3 بعدی نیز کار می کند
ما برای محاسبه ضرب اغضای i تا j به روش زیر عمل می کنیم:
ما قبل از به همین روش تمام جواب های که ضبر j تا k و k تا i که k < j و i < k هست را قبل حساب کرده وذخیره کردیم
حال ما مقدار زیر بدست میاریم برای ضرب  از عضو i تا جه j قرار می دهیم :
min(chain[i, k] + chain[k+1, j] + M[i-1]*M[k]*M[j])
و همچنین مقدار k حالت منیم بدست میاورد ذخیره  می کنیم که بتونیم ترک بک کنیم
این کار ادامه می دهیم که ازز عضو اول تا اخر برسیم.
'''

def chain_matrix(matrix_size:list):
    n = len(matrix_size)
    help_matrix = [[-1 for i in range(n)] for j in range(n)]
    chain = [[0  for i in range(n)] for j in range(n)]

    for size in range(2,n):#at lest we need to 2 matrix to do mutltiplicatoin
        for i in range(n-size+1):
            j = i + size -1
            chain[i][j] =  sys.maxsize# max value
            for k in range( i  , j ):
                min = chain[i][ k] + chain[k + 1][ j] + matrix_size[i - 1] * matrix_size[k] * matrix_size[j]
                if min < chain[i][ j]:
                    chain[i][ j] = min
                    help_matrix[i][ j] = k
    return (chain,help_matrix)

# 50x40 40x30 30x20 20x10
matrix = [50,40,30,20,10]
chain , help =chain_matrix(matrix)
#print(DataFrame(chain))
print(chain[1][len(matrix)-1])

#ramin rowshan 9732491
