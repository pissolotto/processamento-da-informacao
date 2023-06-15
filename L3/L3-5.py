'''
Dado um número natural N, escreva um programa que conte o número de divisores pares de N.

Exemplo: o número 9 tem três divisores (1, 3 e 9), nenhum deles sendo par. Portando, 9 possui 0 divisores pares. Já o número 8 possui quatro divisores (1, 2, 4 e 8), dos quais três são pares. Portanto, 8 possui 3 divisores pares.

Entrada
Um único número inteiro N, tal que 0 ≤ N ≤ 10000.

Saída
Seu programa deve imprimir uma única linha contendo um número que represente a quantidade de divisores pares de N.

Exemplos
Entrada

Saída

8

3

9

0

18

3

79

0

500

8

9800

27
'''

numero = int(input())
divisor = numero
quantidade_divisores = 0

while divisor > 0:
    if numero % divisor == 0 and (divisor) % 2 == 0:
        quantidade_divisores += 1
        #print(divisor)
        divisor -= 1
        
    else:
        divisor -= 1

print(quantidade_divisores)
    