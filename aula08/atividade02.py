# Utilizando função, desenvolva um algoritmo, que solicite ao usuário, o preço e a quantidade, referente a 3 vendas. 
# Para cada venda, o sistema deve calcular o valor total e exibir o resultado.
 
def valor_total(p, q):
    t = p * q
    # print(f'O total é: {total}')
    return t


for n in range(3):
    print(f'Venda {n + 1}')
    preco = float(input('Digite o preço: R$'))
    qntd = float(input('Digite a quantidade: '))
    total = valor_total(preco, qntd)
    print(f'O total é: {total}')