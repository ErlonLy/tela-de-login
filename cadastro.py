from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('DarkBlack') 
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
        [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
        [sg.Checkbox('Salvar o Login?')],
            [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
     break
if eventos == 'Entrar':
    if valores['usuario'] == 'teste' and valores['senha'] == '123456':
        print('Login realizado com sucesso !')