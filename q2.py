from scipy import linalg
import numpy as np

def scipy_linalg_solve(matrix,y):
    return linalg.solve(matrix,y)

def scipy_linalg_inv(matrix,y):
    inv = linalg.inv(matrix)
    return np.matmul(inv,y)


matrix = np.array([[1, 2, 3], [4, 3, 1], [7, 2, 5]])
y = np.array([14,13,26])



print("with scipy_linalg_solve = ",  scipy_linalg_solve(matrix,y))


print("with scipy_linalg_inv = ",scipy_linalg_inv(matrix,y))

'''
فانکشن solve بهتر عمل می کند زیرا 
این فانکشن به طور مستقیم معادله حل می کند ولی
در تابع inv ابتدا ما باید معکسو تابع را بدست بیاورم سپس معکوس را در مقدار y ضرب کنیم که حتی  خود معکوس کردن هزینه بیش تری  
نسبت به مخاسبه مستقیم دارد.
'''
#ramin rowshan 9732491