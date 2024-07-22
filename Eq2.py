#ax²+bx+c=0
import math
a = int(input('Qual valor de a?'))
b = int(input('Qual valor de b?'))
c = int(input('Qual valor de c?'))

delta = b * b - 4 * a * c

if delta < 0:
    print('A equação não possui raizes reais.')
else:
    raiz_delta = math.sqrt(delta)

    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    print(f"x1= {x1} e x2={x2}")
