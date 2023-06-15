'''
Estamos habituados com contagens regressivas. Fazemos contagem regressiva para a chegada de um ano novo, uma data especial, o começo de um filme, dentre outras atividades. Existem diversos aplicativos no mercado com este fim, chamados temporizadores. Uma característica comum a muitos deles é que, a medida que o prazo final se aproxima, a atualização do tempo fica mais frequente. Por exemplo, primeiro começam reportando o tempo em dias, depois em horas, em minutos, e finalmente em segundos. Essa característica deixa o aplicativo mais útil pois nos permite mensurar melhor o tempo que falta até o prazo final.

Um bilionário chamado John Williams precisa de um temporizador para o seu iphone de ouro. O Sr. Williams quer algo exclusivo, porém mais do que um aplicativo desenvolvido exclusivamente para ele, ele quer algo diferente de tudo que existe no mercado (exclusividade é seu nome!). Após consulta com alguns especialistas da UFABC, notou que este é um mercado saturado e que todos os temporizadores que poderiam ser desenvolvidos já o foram, percebeu que a única forma de obter exclusividade seria se o seu temporizador fosse inútil.

Assim, Sr. Williams deseja um temporizador de segundos que passe a atualizar o tempo mais raramente. Ele quer que o intervalo entre cada atualização fique dois segundos maior após cada uma delas. Por exemplo, se ele iniciar o temporizador com 50 segundos, então receberá atualizações dizendo que faltam 50, 48, 44, 38, 30, 20 e 8 segundos (note que os intervalos entre as notificações foram 2, 4, 6, 8, 10 e 12 segundos).

Sabendo do funcionamento de tal aplicativo, desenvolva um programa que exiba em quais segundos o Sr. Williams receberá atualizações, dado que o programa tenha sido inicializado com um tempo igual a N.

Entrada
O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.

Saída
Seu deve escrever a saída conforme os exemplos abaixo.

Exemplos
Entrada

Saída

10



Faltam 10 segundos

Faltam 8 segundos

Faltam 4 segundos

Acabou

50

Faltam 50 segundos

Faltam 48 segundos

Faltam 44 segundos

Faltam 38 segundos

Faltam 30 segundos

Faltam 20 segundos

Faltam 8 segundos

Acabou

'''

segundos = int(input())
decrescimo = 2

while segundos >= 0:
    print(f"Faltam {segundos} segundos")
    segundos -= decrescimo
    decrescimo += 2

print("Acabou")
