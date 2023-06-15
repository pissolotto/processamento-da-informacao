'''
ASCII art é o termo designado para desenhos desenvolvidos utilizando-se somente dos 95 caracteres gráficos (de computadores) definidos pelo Padrão ASCII de 1963. Desenvolva um programa que desenhe ASCII Art de triângulos retângulos isósceles.

ascii

Entrada
O seu programa receber um número natural N que representa a dimensão (em linhas e colunas) dos lados do triângulo que você deverá desenhar.

Saída
O seu programa deve desenhar um ASCII Art de um triângulo de dimensão N como demonstrado nos exemplos abaixo.

Exemplos
Entrada

Saída

3



*

**

***

1

*

7



*

**

***

****

*****

******

*******
'''

i = int(input())

a = 1
while a <= i:
    print("*" * a)
    a += 1