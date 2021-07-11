import math
'''
diagonally dominant matrix
ماتریس مربعی  هست که هر غضو زوی قطر اصلی بزرگ تر(قدرمطلق) مساوی جمع قدرمطلق بقیه اعضای ردیف می باشد
M = Matrix nxn
for each 1<i<= n ==> |Mii| >= zigm(1 to n and i!= j) |Mi,j|

ویزگی
دتریمان ان همیشه مخالف صفر می باشد (nonsingula)
اگر یک ماتریس سمتریک هم باشد که هیچ عضو قطر اصلی نامنفی باشید در این صورت zTMz >0 به شرط z نامساوی 0 باشد(M ماتریس بیان شده است
'''

def is_diagonally_dominant(matrix:list):
    for i in range (len(matrix)):
        my_sum = 0
        for j in range(len(matrix)):
            if i !=j :
                my_sum += abs(matrix[i][j])
        if abs(matrix[i][i]) < my_sum:
            return False

    return True

print(is_diagonally_dominant([[5,3,2],[3,9,2],[2,1,6]]))

#|-8| +|4| <= |9| ==> wrong
print(is_diagonally_dominant([[7,-4,2],[-8,11,4],[4,9,15]]))

#ramin rowshan 9732491