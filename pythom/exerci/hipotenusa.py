from math import hypot,sqrt
w = float(input('digite o cateto oposto    : '))
a = float(input('digite o cateto adjacente : '))
h = a**2 + w**2 
print('a hipotenusa é {:.2f}'.format(sqrt(hypot(h))))


co = float(input('digite o cateto oposto    : ')) 
ca = float(input('digite o cateto adjacente    : '))
hy = hypot(co, ca)
print('a hipotenusa é {:.2f}'.format(hy))
