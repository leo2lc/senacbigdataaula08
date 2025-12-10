# Crie um programa em Python que cadastre os dados de 3 vendedores.
# Cada vendedor deve ser armazenado, contendo as seguintes informações:

# nome
# vendas - armazenar 5 vendas, representando os valores das vendas realizadas
# total - armazenar a soma de todas as vendas (calcular)
# media - armazenar a média das vendas (calcular)

# Após o cadastro dos 3 vendedores, o prgrama dve exibir os dados completos de cada um : Nome, Lista de vendas, Total e Média.

vendedores = []

for n in range(3):
    print(f'Vendedor {n + 1}')
    nome = input('Nome do vendedor: ')

    vendas = []
    for v in range(5):
        venda = float(input(f'Valor da venda {v + 1}: R$ '))
        vendas.append(venda)
    
    total = sum(vendas)
    media = total / len(vendas)
    print(f'O total de vendas foi {total:.2f}')
    print(f'A média de vendas foi {media:.2f}')
    
    vendedor = {
        'Nome': nome,
        'Vendas': vendas,
        'Total': total,
        'Media': media
    }

    vendedores.append(vendedor)

for vendedor in vendedores:
    print(f'Nome: {vendedor["Nome"]},\n Vendas: {vendedor["Vendas"]},\n Total: {vendedor["Total"]},\n Média: {vendedor["Media"]}')
# print(vendedores)