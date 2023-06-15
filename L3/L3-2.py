'''
Escreva um programa que apresente a tabuada de um número.

Entrada
O seu programa receberá um inteiro positivo N e um inteiro positivo M.

Saída
O seu programa deve imprimir a tabela de multiplicação do número N, começando de 0 e terminando em M.

Exemplos
Entrada

Saída

3

5

3 x 0 = 0

3 x 1 = 3

3 x 2 = 6

3 x 3 = 9

3 x 4 = 12

3 x 5 = 15

7

12

7 x 0 = 0

7 x 1 = 7

7 x 2 = 14

7 x 3 = 21

7 x 4 = 28

7 x 5 = 35

7 x 6 = 42

7 x 7 = 49

7 x 8 = 56

7 x 9 = 63

7 x 10 = 70

7 x 11 = 77

7 x 12 = 84
'''


multiplicador = int(input())
multiplicando = int(input())

n = 0
while n <= multiplicando:
    print(f"{multiplicador} x {n} = {multiplicador * n}")
    n += 1
    

