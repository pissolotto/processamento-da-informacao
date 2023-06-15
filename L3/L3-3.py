"""Antes da popularização dos computadores pessoais, vendinhas e mercados computavam o valor total das compras de seus clientes usando máquinas de somar. Tais máquinas eram equipamentos totalmente mecânicos e tinha um funcionamento bem simples, bastava digitar o valor do produto e puxar uma manivela para que tal valor fosse adicionado ao valor do somatório dos produtos.

somador

Desenvolva um programa que simule o funcionamento de uma máquina de somar.

Entrada
O seu programa receberá um número inteiro não negativo N que denota a quantidade de números que seu programa receberá para computar o valor total da soma. Na sequência seu programa receberá N números reais.

Saída
O seu programa deve imprimir a frase “Total: ” seguida do valor da soma dos N números reais (com duas casas decimais de precisão).

Exemplos
Entrada

Saída

3

7.00

1.50

2.25

Total: 10.75

5

1.25

5.70

2.56

9.99

3.00

Total: 22.50
"""

quantidade = int(input())
i = 1
soma = 0

while i <= quantidade:
    numero = float(input())
    soma += numero
    i += 1
    print(soma)


print("Total: %.2f"%soma)