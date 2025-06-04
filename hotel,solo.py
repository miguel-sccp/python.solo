print('Seja bem-vindo! Faça seu cadastro.')


pessoas = {}
nomes = []

for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = input(f"Digite a idade do(a) {nome}: ")
    pessoas[nome] = idade
    nomes.append(nome)


quartos_dispo = ['', 'simples', 'duplo', 'luxo']
preco = ['', 100, 150, 250]

print('\nEscolha seu quarto através do ID 1-3')
print('Quartos disponíveis:')
print(f"1 - {quartos_dispo[1]}: R$ {preco[1]}/dia")
print(f"2 - {quartos_dispo[2]}: R$ {preco[2]}/dia")
print(f"3 - {quartos_dispo[3]}: R$ {preco[3]}/dia\n")


pedido1 = int(input(f"{nomes[0]}, digite o ID do quarto desejado (1-3): "))
pedido2 = int(input(f"{nomes[1]}, digite o ID do quarto desejado (1-3): "))
pedido3 = int(input(f"{nomes[2]}, digite o ID do quarto desejado (1-3): "))


carrinho = [quartos_dispo[pedido1], quartos_dispo[pedido2], quartos_dispo[pedido3]]
meu_total = [preco[pedido1], preco[pedido2], preco[pedido3]]


dias1 = int(input(f"Quantos dias {nomes[0]} irá ficar? "))
dias2 = int(input(f"Quantos dias {nomes[1]} irá ficar? "))
dias3 = int(input(f"Quantos dias {nomes[2]} irá ficar? "))


print("\n--- RESUMO DA RESERVA ---")
print(f"{nomes[0]} irá ficar no quarto {carrinho[0]} por {dias1} dias. Total: R$ {meu_total[0] * dias1}")
print(f"{nomes[1]} irá ficar no quarto {carrinho[1]} por {dias2} dias. Total: R$ {meu_total[1] * dias2}")
print(f"{nomes[2]} irá ficar no quarto {carrinho[2]} por {dias3} dias. Total: R$ {meu_total[2] * dias3}")
print("\nObrigado por reservar conosco!")
