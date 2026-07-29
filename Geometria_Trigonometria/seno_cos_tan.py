import math
angulo_graus = int(input('Digite o valor do ângulo: '))
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'O ângulo é: {angulo_graus}º')
print(f'O seu valor de seno é {seno:.2f}')
print(f'O seu valor de cosseno é {cosseno:.2f}')
print(f'O seu valor de tangente é {tangente:.2f}')

