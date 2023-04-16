import PySimpleGUI as sg
import robo_speaker as r
l1=[["male"],["female"]]

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('enter the rate: '),sg.Slider(range=(10, 200), default_value=12,
   expand_x=True, enable_events=True,
   orientation='horizontal', key='Rate'),sg.Button('HEAR SAMPLE')],
            [sg.Text('Enter the text', ), sg.InputText(key='TEXT')],
            [sg.Text("voice options: "),sg.DropDown(l1,key="voice")],
            [sg.Text("enter the name of the file"),sg.InputText(key="Name")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event =='HEAR SAMPLE':
        x=int(values['Rate'])
        if values['voice'] == ['female']:
            y=1
            
        else:
            y=0
        r.test_audio(x,y)
    if event=='Ok':
        if values['voice'] == ['female']:
            voice=1
        else:
            voice=0
        r.save_file(int(values['Rate']),text=values["TEXT"],voice=voice,Name=values["Name"])


window.close()
