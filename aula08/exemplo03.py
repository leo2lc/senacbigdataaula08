# def saudacao(n, i):
#     print(f'Olá {n}, você tem {i} anos')

# nome = input('Informe o nome: ')
# idade = input('Informe o nome: ')
# saudacao(nome, idade)
#---------------------------------------------

def soma(n1, n2):
    total = n1 + n2
    print(f'O total é: {total}')


def maior_numero(a, b):
    if a > b:
        print(f'O maior é {a}')
    elif b > a:
        print(f'O maior é {b}')
    else:
        print('Os números são iguais')


def somar_numeros(x, y):
    total = x + y
    print(total)

#---------programa principal-------------------

# num1 = float(input('Digite um número: '))
# num2 = float(input('Digite um número: '))
# soma(num1, num2)

#---------descobre o maior---------------------

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

maior_numero(numero1, numero2)

#---------Soma 3 pares de números--------------

for n in range(3):
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    somar_numeros(n1, n2)