from funçoes import exc
import PySimpleGUI as sg

obj = exc.Execucao()
# obj.MenuS()
e = ''

# criando a janela (GUI)
sg.theme('Tan Blue')  # Definindo um tema para a janela

# Desingn da janela.
layout = [[sg.Text('Nome:', size=(6, 1)), sg.InputText(size=(30, 1), key='-NOME-')],
          [sg.Text('Qtd:', size=(6, 1)), sg.InputText(size=(30, 1), key='-QUANTIDADE-')],
          [sg.Text('Tipo:', size=(6, 1)), sg.InputText(size=(30, 1), key='-TIPO-')],
          [sg.Button('Cadastrar', button_color='black on white', font=['Comics', 12]),
           sg.Button('Sair', button_color='black on white', font=['Comics', 12]),
           sg.Button('Ver Registros', button_color='black on white', font=['Comics', 12]),
           sg.Button('Deletar', button_color='black on white', font=['Comics', 12])]]

window1 = sg.Window('Cadastro de Produto', layout)
window2_active = False

while True:
    event1, values1 = window1.read()
    # if user closes window or clicks exit
    if event1 == sg.WIN_CLOSED or event1 == 'Sair':
        break

    if event1 == 'Cadastrar':
        n1 = values1['-NOME-']
        n2 = values1['-QUANTIDADE-']
        try:
            # inserindo dados na tabela
            obj.InsertS(n1, n2)
            sg.popup('Cliente cadastrado com sucesso!')
            window1['-NOME-'].update('')
            window1['-QUANTIDADE-'].update('')
            window1['-TIPO-'].update('')
        except e as Argument:
            print(f'Erro ao gravar os dados:\n{e}')
            sg.popup(f'{e}')

    if event1 == 'Ver Registros' and not window2_active:
        window2_active = True
        window1.Hide()

        # SEMPRE CRIAR LAYOUT NOVO, NUNCA REUTILIZAR
        layout2 = [[sg.Text('TIPO DE FILTRO', font=('Helvetica', 14), justification='left')],
                   [sg.Radio('Id', 'loss', default=True, size=(5, 1), font=['Comics', 14]),
                    sg.Radio('Tipo', 'loss', size=(5, 1), font=['Comics', 14])],
                   [sg.Text('Busca:', size=(5, 1), font=['Comics', 13]),
                    sg.InputText(size=(40, 1), key='-BUSCA-', font=['Comics', 13]),
                    sg.Button('Filtrar', button_color='black on light blue', font=['Comics', 12])],
                   [sg.MLine(key='-ML1-' + sg.WRITE_ONLY_KEY, size=(80, 15), font='Any 13')],
                   [sg.Button('Sair', button_color='black on red', font=['Comics', 12])]]

        window2 = sg.Window('Ver/Filtrar Registros', layout2, finalize=True)

        # Preenchendo na primeira execução
        window2['-ML1-' + sg.WRITE_ONLY_KEY].print('\nOS DADOS SALVOS NO BANCO DE DADOS SÃO:\n', text_color='yellow',
                                                   background_color='black')
        n = obj.ExecuteS()
        letra = 'Quantidade:'
        for row in n:
            window2['-ML1-' + sg.WRITE_ONLY_KEY].print(
                f'Id: {row[0]:<3} Produto: {row[1]:<20} {letra:>10} {row[2]}', text_color='black')

        #Laço da segunda janela
        tipoBusca = True
        while True:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED or event2 == 'Sair':
                window2.Close()
                window2_active = False
                window1.UnHide()
                break

            if event2 == 'Id':
                tipoBusca = True
            if event2 == 'Tipo':
                tipoBusca = False

            if event2 == 'Filtrar' and tipoBusca:
                n1 = values2['-BUSCA-']
                n = obj.ExecuteF(n1)
                for row in n:
                    window2['-ML1-' + sg.WRITE_ONLY_KEY].print(
                        f'Id: {row[0]:<3} Produto: {row[1]:<20} {letra:>10} {row[2]}', text_color='black')

            if event2 == 'Filtrar' and not tipoBusca:
                n1 = values2['-BUSCA-']
                n = obj.ExecuteF(n1)
                # window2.keep_on_top_clear()
                for row in n:
                    window2['-ML1-' + sg.WRITE_ONLY_KEY].print(
                        f'Id: {row[0]:<3} Produto: {row[1]:<20} {letra:>10} {row[2]}', text_color='black')