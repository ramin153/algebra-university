def inner_product(vector1: list, vector2: list, size: int = 3):
    '''
    مقدار از پیش تعیین شده برای سایز 3 هست
    پس در واقع در این فور ما ایتم های اول تا سوم(ایندکس 0 تا 2) تو لیست متاقبل را در هم ضرب می کنیم
    و سپس ایتم ها را جمع می کنیم
    x1 * y1 + x2 * y2 + x3 * y3 = result
    که جواب برابر ضرب داخلی یک وکتر 3 بعدی می باشد
    '''
    result = 0
    for i in range(0, size, 1):
        result += vector2[i] * vector1[i]
    return result


if __name__ == "__main__":
    print(inner_product([1, 2, 3], [3, 2, 1]))
    print(inner_product([1, 1, 1], [8, 8, 8]))
    print(inner_product([1, 0, 0], [0, 0, 1]))
    print(inner_product([1, 2, 3], [100000, 1, 1]))
    print(inner_product([10, 20, 30], [3, 2, 1]))
