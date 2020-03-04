#Pi sayısının virgülden sonra 19 basamağı
from decimal import *
getcontext().prec = 20
n,p,p1 = 1,1,0
while (abs(p1-p) > 0.000001):
    p=p1
    p1 += Decimal((4/(2*n-1))*((-1)**(n+1)))
    n+=1
    print(p," ",p1)
print(p)
