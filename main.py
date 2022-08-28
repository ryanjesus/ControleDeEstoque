from funçoes import exc

obj = exc.Execucao

while True:
    obj.MenuS()
    while True:
        n = input('Menu: ')
        if n in (1, 2, 3, 4, 0):
            break
        else:
            print('Por favor digita o numero do Menu')
    if n == 0:
        print('Saindo...')
        break
    elif n == 1:
        obj.ExecuteS()
    else:
        print()
