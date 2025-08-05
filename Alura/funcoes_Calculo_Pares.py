valores = input("Digite os números separados por espaço: ").split()

pares = filter(lambda x: int(x) % 2 == 0, valores)

print(f"Números pares:", " ".join(pares))