#Radix question 1
"""1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?"""
############################################################################################################################

#CODE:

index = 13
k = 0
sum = 0

while k < index:
    k+=1
    sum+=k

print(sum)
#Result: 91
