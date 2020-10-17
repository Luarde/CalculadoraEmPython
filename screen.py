# based on https://github.com/Ybenson

import PySimpleGUI as sg

#Configuração de botões
numButton: dict = {'size':(7,2)}
equalButton: dict = {'size':(15,2),'focus':True}

# Layout
layout: list = [
    [sg.Text('0.00', size=(50,1), justification='center', relief='sunken', key="_DISPLAY_")],
    [sg.Button('C',**numButton), sg.Button('/',**numButton), sg.Button('*',**numButton), sg.Button('-',**numButton)],
    [sg.Button('7',**numButton), sg.Button('8',**numButton), sg.Button('9',**numButton), sg.Button('+',**numButton)],
    [sg.Button('4',**numButton), sg.Button('5',**numButton), sg.Button('6',**numButton)],
    [sg.Button('1',**numButton), sg.Button('2',**numButton), sg.Button('3',**numButton)],
    [sg.Button('0',**numButton), sg.Button('=',**equalButton, bind_return_key=True)]

]

# Janela
window: object = sg.Window('Calculadora', layout=layout, size=(300,300), return_keyboard_events=True)

# Função para cálculos
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

# Helper Functions
def format_number() -> float:
    ''' Create a consolidated string of numbers from front and back lists '''
    return float(''.join(var['front']) + '.' + ''.join(var['back']))
    
def update_display(display_value: str):
    ''' Update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)


#-----CLICK EVENTS
def number_click(event: str):
    ''' Number button button click event '''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())


def clear_click():
    ''' CE or C button click event '''
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 


def operator_click(event: str):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


def calculate_click():
    ''' Equals button click event '''
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()    
    except:
        update_display("ERROR! DIV/0")
        clear_click()


#-----MAIN EVENT LOOP------------------------------------##
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['Escape:27','C',]: # 'Escape:27 for keyboard control
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    