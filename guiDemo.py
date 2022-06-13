import PySimpleGUI as sg


def createWindow() -> None:
    sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
