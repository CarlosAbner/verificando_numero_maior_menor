# biblioteca de tempo, para a função de validação dos dados e importando somente a dependencia sleep!
from time import sleep

print('=-=-'*16)
print('Digite 7 números inteiros para identificar o Maior e o Menor')
print('=-=-'*16)

#variavies para armazenar os valores de n° maior e n° menor
maior = 0
menor = 0

# fazendo a contagem para a digitacao dos 7 valores e também validando cada N° digitado 
for n in range(1, 8):
    num = int(input('Digite o {}° número: '.format(n)))
    # verificando e armazenando cada numero como maior ou menor nas variaveis em cima do for
    if n == 1:
        maior = num
        menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
#usando o sleep para "validar" os dados
print('Analisando...')
sleep(1)

# retornando o resultado da avaliação!
print('=-=-'*16)
print('O número {} foi o maior digitado'.format(maior))
print('O número {} foi o menor digitado'.format(menor))
print('=-=-'*16)
