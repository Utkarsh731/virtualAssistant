import wolframalpha
import wikipedia
import PySimpleGUI as sg
import pyttsx3

engine=pyttsx3.init()

client=wolframalpha.Client("Y93EGX-V3WRJLWQXG")
sg.theme('DarkBLue')
layout = [
            [sg.Text('Search'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Jarvis here', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        res = client.query(values[0])
        engine.say(next(res.results).text)
        sg.PopupNonBlocking(next(res.results).text)
        engine.runAndWait()
    except:
        wikipedia_response = wikipedia.summary(values[0], sentences=3)
        engine.say(wikipedia_response)
        sg.PopupNonBlocking(wikipedia_response)
        engine.runAndWait()


window.close()
