import counterUtils as cu

from pynput import keyboard

def on_press(key):

    if cu.getDicVal("kill") is not None:
        return false

    try:
        if key.char == ',':
            cu.incrementValue("cc", printOpt=True)
        elif key.char == '.':
            cu.decrementValue("cc", printOpt=True)
    except:
        return

def keylistenerThread():

    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()