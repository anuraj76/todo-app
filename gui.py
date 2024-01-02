import functions

import PySimpleGUI as sg



label  = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window('My todo App', layout=[[[label],[input_box,add_button]]])
window.read()
print("Hello")
window.close()