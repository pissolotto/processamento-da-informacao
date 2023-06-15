'''
A ideia de múltiplo e divisor é conhecida desde a Grécia Antiga. Naquela época, os sábios davam tanta importância aos números que lhes atribuíam características humanas. Para ter uma ideia, eles agrupavam os números em masculinos (os ímpares) e femininos (os pares). Daí que surgiram também os conceitos de números abundantes e perfeitos.

Agora falaremos de outro conceito criado nesta época, a de números amigos. Dois números são amigos se a soma dos divisores próprios de um for igual ao outro e vice-versa. Por exemplo, 220 e 284, são números amigos, pois os divisores próprios de 220 somam 284 e os divisores próprios de 284 somam 220.

Faça um programa que dado dois números naturais determine se eles são amigos.

Entrada
A entrada consiste de dois números inteiros X e Y, dados nesta respectiva ordem.

Saída
A saída consiste de uma única linha contendo a frase “amigos”, caso X e Y sejam números amigos, e a frase “nao amigos”, caso contrário.

Exemplos
Entrada

Saída

54

45

nao amigos

150

260

nao amigos

220

284

amigos

1

10

nao amigos

1184

1210

amigos

35

22

nao amigos
'''

primeiro = int(input())
segundo = int(input())

def comparar(primeiro: int, segundo:int) -> str:
    soma_primeiro = 0
    divisor = primeiro
    while divisor > 0:
        if primeiro % divisor == 0 and primeiro != divisor:
            soma_primeiro += divisor
            divisor -= 1
        
        else:
            divisor -= 1
    
    if soma_primeiro != segundo:
        return "nao amigos"
    
    else:
        soma_segundo = 0
        divisor = segundo
        while divisor > 0:
            if segundo % divisor == 0 and segundo != divisor:
                soma_segundo += divisor
                divisor -= 1
            else:
                divisor -= 1
    
    if soma_segundo != primeiro:
        return "nao amigos"
    
    else:
        return "amigos"
    

print(comparar(primeiro, segundo))
