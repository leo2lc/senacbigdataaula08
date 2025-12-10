alunos = [] # Lista onde as informações dos alunos serão armazenadas

for n in range(3): # For para a quantidade já determinada de vezes que vai executar o código abaixo
    print(f'\n----- Aluno {n + 1} -----')
    nome = input('Informe o nome do aluno: ')

    notas = []
    for i in range(3):
        nota = float(input(f'Informe a nota {i + 1}: '))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    print(media)

    # Agrega as variáves no item "aluno" e esse item será enviado para a lista
    aluno = {
        'Nome': nome,
        'Notas': notas,
        'Media': media
    }

    alunos.append(aluno) # Adiciona os elementos do dicionário na lista

# Exibindo os dados
for estudante in alunos:
    print(f'Nome: {estudante["Nome"]}, Notas: {estudante["Notas"]}, Média: {estudante["Media"]}')
    #print(f'Notas: {estudante["Notas"]}')
    #print(f'Média: {estudante["Media"]}')
