from scipy import sparse
import numpy as np
import random

'''اسپارس وکتور: یک وکتور هست که بیش تر ایتم هاش رو مقدار صفر تشکیل داره یعنی اکثر اعضای ان داری مقدار ثابت صفر و به 
گونه ها مختلف قابل صرف نظر هستن و ما باید سعی کنیم که چطور این وکتور ذخیره سازی کنیم که بهینه باشد و  یک روش بهینه 
این است که فقط اعضای غیر صفر را نگه داری کنیم 

'''

'''
به وسیله تابع اسپارس ما یک وکتر 5 بعدی می سازیم که به خاطر تابع راند اینت بین 0 تا که در 0.2 ضرب شده احتمال بین 
0 تا 2 عضو مقدار غیر صفر دارند و باز تعداد اعضای غیر صفر بیش تر اعضای دارای صفر می باشد.
بعد ما تعداد اعضای غیر صفر ان می شماریم و نشان می دهیم
'''
vector = np.array(sparse.random(1, 5,.2 * random.randint(0,2), ).A[0])

print(np.count_nonzero(vector))