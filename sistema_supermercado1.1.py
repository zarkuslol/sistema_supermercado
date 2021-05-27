# Sistema para supermercado/empório/mercearia e afins
# importações do programa
import os

# NÃO MEXA NESSA PARTE DE CIMA, PELO AMOR DE DEUS
contador = 0
titulo = 'NOME DA EMPRESA'

# programa
while contador == 0:
    # variáveis importantes, não mexa nelas!!
    soma = 0
    preco2 = 0
    # ---------------------------------------
    print('-=-' * 20)
    print(titulo.center(50))  # título
    print('-=-' * 20)
    print('')
    qtd = int(input('Unidades a serem compradas: '))  # unidades = um produto só ou um conjunto de produtos do mesmo tipo
    dup = input('Existem produtos repetidos ou mais? [1] Sim ou [2] Não: ')  # condicional para produtos repetidos

    # para caso houver produtos iguais na compra

    if dup == '1':
        print('')
        grupos = int(input('Quantos grupos de produtos repetidos existem? '))  # grupos = conjunto de produtos do mesmo tipo
        for c in range(1, grupos+1, 1):
            qtd2 = int(input('Número de produtos do grupo {}: '.format(c)))   # quantidade de produtos no conjunto
            val = float(input('Preço unitário de um produto: R$'))   # preço de apenas um produto
            preco2 = qtd2 * val
            print('Valor do grupo: R${:.2f}'.format(preco2))
            print('')
        for a in range(1, qtd+1, 1):
            preco = float(input('Valor da unidade {}: R$'.format(a)))
            soma += preco
        print('\nTotal da compra: R${:.2f}'.format(soma))
        input('Pressione ENTER para repetir ou saia do terminal')  # repete ou sai do sistema
        os.system('cls')

    # caso não tenha, o programa segue sem condicional

    else:
        for a in range(1, qtd+1, 1):
            preco = float(input('Valor da unidade {}: R$'.format(a)))
            soma += preco
        print('\nTotal da compra: R${:.2f}'.format(soma))
        input('Pressione ENTER para repetir ou saia do terminal')  # repete ou sai do sistema
        os.system('cls')
# fim do programa
