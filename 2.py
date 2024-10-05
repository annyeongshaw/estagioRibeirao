""" Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. """


def quantidadeDeA(string):
    vezesA = string.lower().count('a')
    
    if vezesA > 0:
        return f"A letra 'a' aparece {vezesA} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."


texto = input("Digite uma string: ")
print(quantidadeDeA(texto))
