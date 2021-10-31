import PySimpleGUI as sg

layout = [
    [sg.Text('Enter the First Number: '), sg.InputText()],
    [sg.Text('Enter the Second: '), sg.InputText()],
    [sg.Button('Add'), sg.Button('Quit')]
]

window = sg.Window('Adder!', layout)

while True:
    events, values = window.read()
    if events in (None, 'Quit'):
        break
    if events == "Add":
        a = int(values[0])
        b = int(values[1])
        c = a + b
        sg.Popup(f"{a} + {b} = {c}")

window.close()
