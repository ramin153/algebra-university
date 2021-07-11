import numpy as np
'''
به وسیله np.array(list) ما می تونیم به سوال 4 پاسخ بدهیم
'''
A = np.array([[0, 1, 0], [-1, 0, 1], [0, -1, 0]])
B = np.array([[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
x = np.array([1,2, 2])
y = np.array([-1,2,3])

if __name__ == "__main__":

    '''
    موارد گنگ توضح داده خواهد شد
    '''
    print("q4\n")
    print(A)
    print(B)
    print(x)
    print(y)
    print("\nq5\n")
    print("x+y",x+y,sep="\n")
    print("\n3x+4y",(x*3) + (4*y),sep="\n")
    print("\n||x||", np.linalg.norm(x), sep="\n")#تابع نرم برای محاسبه اندازه هست
    print("\nrms(x)",np.sqrt(np.mean(np.square(x ))), sep="\n")
    '''
    چون تابع rms وجود ندارد پس ما ابتدا تمام اعضا رو بتوان دو می رسونیم بعد میانگینشون حساب میکنیم و در اخر ازش جز می گیریم
    sqrt ((zigma i = 0 to n (xi * xi)) / n) 
    '''
    print("\nunit vector x",x/np.linalg.norm(x), sep="\n")#برای محاسبه مقدار بردار یکه کافی هست برداز بر اندازه (نرم) تقسیم کنیم
    print("\nangle between x and y",np.rad2deg(np.arccos(x.dot(y) / (np.linalg.norm(x)*np.linalg.norm(y)))), sep="\n")
    '''چون تابع برای محاسبه مستقیم زاویه وجود نداره پس ما ابتدا ضرب نقطه ای یا لینر پرادکت دو بردار انجام می دهیم سپس 
    بر ضرب انداز دو بردار تقسیم می کنیم x.y/||x||*||y||=result بعد مقدار بدست اماد جون مقدار cos زاویه هست و باید 
    برگد ، به تابع کوسینوس اینور یا across پاس می دهیم تا مقدار زاوبه بدست بیاید اما زاوبه به رادیان هست پس ما به 
    درجه باز می گردانیم '''

    print("\nshape of x",np.shape(x), sep="\n")
    print("\nvector perpendicular",np.cross(y, x), sep="\n")
    print("\nA.B",np.matmul(A,B), sep="\n")
    print("\nAx",np.matmul(A,x), sep="\n")
    print("\ntranspose A ",np.transpose(A), sep="\n")


