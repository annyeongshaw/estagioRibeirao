""" Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. """

def sequenciaDeFibonacci(n):
    inicio = [0, 1] 
    while inicio[-1] < n:  
        inicio.append(inicio[-1] + inicio[-2])
    return inicio

def fibonacci(n):
    inicio = sequenciaDeFibonacci(n)
    if n in inicio:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(fibonacci(numero))