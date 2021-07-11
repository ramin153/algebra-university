def inner_product(vector1: list, vector2: list, size: int = 3):
    result = 0
    for i in range(0, size, 1):
        result += vector2[i] * vector1[i]
    return result


def vector_multiplication(matrix:list,vector:list,size:int = 3):
    result = []
    '''
    ضرب ماتریس یعنی سطر ماتریس اول در ستون ماتریس دوم
    چون معادله به صورت ax هست پس سطر های ماتریس a در وکتر x ضرب می شود 
    و ضرب شدن یعنی ضرب ایتم های متناظر و جمع کردن ان های که به عبارت دیگر لینر پراداکت در حال انجام است
    و جواب نهایی ما یک ماتریس با 3 سطر و یک ستون می باشد
    '''
    for i in range(0,size,1):
        result.append([inner_product(matrix[i],vector,size)])

    return result


if __name__ == "__main__":
    print(vector_multiplication([[1,1,1],[2,2,2],[3,3,3]],[1,2,3]))
    print(vector_multiplication([[1,2,3],[4,5,6],[7,8,9]],[1,1,1]))
    print(vector_multiplication([[1,-3,4],[5,6,-7],[3,2,12]],[-1,5,8]))