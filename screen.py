# based on https://github.com/Ybenson

import PySimpleGUI as sg

# Layout
layout: list = [
    [sg.Text('0.00', size=(50,1), justification='')]
    [sg.Button('C'), sg.Button('/'), sg.Button('*'), sg.Button('-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3')],
    [sg.Button('0'), sg.Button('=', bind_return_key=True)]

]

window: object = sg.Window('Calculadora', layout=layout, size=(580,660), return_keyboard_events=True)

