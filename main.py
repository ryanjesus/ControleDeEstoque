from funçoes import exc

obj = exc.Execucao()

obj.MenuS()

while True:

    while True:
        print('-'*20)
        n = input('Menu: ')
        print('-' * 20)

        if n in '123450':
            break
        else:
            print('Por favor digita o numero do Menu')

    if n == '0':
        print('Saindo...')
        break
    elif n == '1':
        obj.MenuS()

    elif n == '2':
        e = 'ESTOQUE'
        print(f'{e:^20}')
        obj.ExecuteS()

    elif n == '3':

        e = 'ATUALIZAR PRODUTO'
        print(f'{e:^20}')

        while True:
            while True:
                n1 = input('Código do produto: ')
                n2 = input('Quantidade do produto: ')

                if n1.isnumeric() and n2.isnumeric():
                    break
                else:
                    print('Apenas numeros!!')
            obj.UpdateS(n2, n1)
            obj.ExecuteF(n1)
            break

    elif n == '4':

        e = 'INSERIR PRODUTO'
        print(f'{e:^20}')

        while True:
            n1 = input('Nome do produto: ')

            while True:
                n2 = input('Quantidade incial: ')

                if n2.isnumeric():
                    break
                else:
                    print('Apenas numeros')
            obj.InsertS(n1, n2)
            print(f'Produto {n1} inserido')
            break

    elif n == '5':

        e = 'DELETAR PRODUTO'
        print(f'{e:^20}')

        while True:

            while True:
                n1 = input('Código do produto: ')
                if n1.isnumeric():
                    break
                else:
                    print('Apenas numeros')
            obj.DeleteS(n1)
            print(f'Código {n1} deletado')
            break
