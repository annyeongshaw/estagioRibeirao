""" Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? Ao final a soma será 77 """

indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)