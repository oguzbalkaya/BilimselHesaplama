#euler sayısı
#Virgülden sonra 16 basamak.
from math import factorial
n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += 1/factorial(n)
    n += 1
print(e)

#Virgünden sonra daha fazla basamak

from decimal import *
getcontext().prec = 20 #Toplam 20 basamaklı.
n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += Decimal(1/factorial(n))
    n += 1
print(e)
