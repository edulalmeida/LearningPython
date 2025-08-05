"""

Usuário deve acertar um número secreto.

"""

numero = int(input("\nDigite um número: "))

secret = 777

while numero != secret:
    print("\nVocê não acertou o número secreto: ")
    
    numero = int(input("\nDigite um número: "))

print("\nParabéns, vc acertou o número secreto!!!")
