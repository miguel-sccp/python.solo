print("Seja bem-vindo")
numero = []

for i in range(3):
    while True:
        entrada = input(f"Digite o {i+1}º número: ")
        try:
            valor = int(entrada)
            numero.append(valor)
            break
        except ValueError:
            print("Digite apenas números inteiros idiota.")

print("Lista:", numero)
print("Maior número:", max(numero))
print("Menor número:", min(numero))
print("Soma de todos os números:", sum(numero))
print("Quantidade de números no total:", len(numero))
