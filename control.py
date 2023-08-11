from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlmouse():
    mouse=Controller()
    mouse.position=(10,20)

def controlkeyboard():
    keyboard=Controller()
    keyboard.type("I m awesome")

controlkeyboard()