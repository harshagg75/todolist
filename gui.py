import functions
import PySimpleGUI as xd

label = xd.Text("Type in a To-Do")
input_box = xd.InputText(tooltip= "Enter the To-DO")

add_button = xd.Button("ADD")

window = xd.Window("TO-DO App", layout=[[label],[input_box,add_button]])
window.read()
window.close()
