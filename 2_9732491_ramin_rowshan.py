import math


def inner_product(vector1: list, vector2: list, size: int = 3):
    result = 0
    for i in range(0, size, 1):
        result += vector2[i] * vector1[i]
    return result


def vector_size(vector1: list, size: int = 3):
    '''

    ما در این تابع ابتدا توان 2 اعضا که تعداد دیفالت ان 3 هست را با هم جمع می کنیم
    x1 ** 2 + x2 ** 2 + x3**2 = sum_pow
    سپس از ان جز می گریم که مقدار اندازه وکتر با همان نرم ان بدست می اید
    '''
    sum_pow = 0
    for i in range(0, size, 1):
        sum_pow += vector1[i] * vector1[i]

    return math.sqrt(sum_pow)


def vector_angle(vector1: list, vector2: list, size: int = 3):
    # cos @ = a.b/||a||||b||
    '''

    ما می دانیم به روش که در بالا هست می توان زاویه بین دو وکتر پیدا کنیم
    بنابر این به وسیله فانکشن اینر پروداکت مقدار a.b
    و به وسیله فانکشن وکتر سایز مقدار ||a|| و ||b|| بدست می اوریم
    سپس معادله a.b/||a||*||b||=acos
    قرار می دهیم که مقدار رادیان زاویه را به ما می دهد
    پس به وسیله تابع مت این مقدار را به درجه تبدیل می کنیم
    '''
    try:
        return math.degrees(
            math.acos(
                ((inner_product(vector1, vector2, size)) / (vector_size(vector1, size) * vector_size(vector2, size)))))
    except ValueError:
        return 0


if __name__ == "__main__":
    print(vector_angle([1, 2, 3], [3, 2, 1]))
    print(vector_angle([1, 1, 1], [8, 8, 8]))
    print(vector_angle([1, 0, 0], [0, 0, 1]))
    print(vector_angle([1, 1, 1], [-3, -3, -3]))
    print(vector_angle([3, 4, -1], [2, -1, 1]))
