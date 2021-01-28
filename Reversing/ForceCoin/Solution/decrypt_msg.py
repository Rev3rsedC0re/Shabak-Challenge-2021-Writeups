from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as Mouse
from pynput.mouse import Button as Btn
from pynput.mouse import Listener
import time

keyboard = Controller()
mouse = Mouse()

chars='abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&&*()}:|\/.~;-<>,'
arr=[(980,300),(980,335),(980,370),(980,405),(980,440),(980,475)]

#flag = 'flag{L3m0n-SqueeZy}'
flag='flag{'
def on_click(x, y, button, pressed):
    if not pressed:
        arr.append((x,y))
        return False

def read_custom():
    with open('db.txt','r') as file:
        c_f = str(file.read())
        c_msg = c_f[c_f.index('[')+1:int(c_f.index(']'))]
        last_letter = c_msg.split(', ')[-1]
        return last_letter

def create_transaction(w):
    global arr
    time.sleep(0.3)
    mouse.position = arr[2]
    time.sleep(0.3)
    mouse.click(Btn.left, 1)
    time.sleep(0.3)
    time.sleep(1)
    keyboard.type(w)
    time.sleep(0.3)
    mouse.position = arr[4]
    time.sleep(0.3)
    mouse.click(Btn.left, 1)
    time.sleep(0.3)
    mouse.position = arr[3]
    time.sleep(0.3)
    mouse.click(Btn.left, 1)
    time.sleep(0.3)
    mouse.position = arr[5]
    time.sleep(0.3)
    mouse.click(Btn.left, 1)
    mouse.position = arr[2]
    time.sleep(0.3)
    mouse.click(Btn.left, 1)
    time.sleep(0.3)
    for i in range(len(w)):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    time.sleep(0.5)
    for i in range(len(w)):
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    time.sleep(0.5)
    
with open('save.txt','r') as file:
	f = str(file.read())
	msg = f[f.index('[')+1:int(f.index(']'))]
	letters = msg.split(', ')

	
#time.sleep(2)
#create_transaction('flag{')
found = True
while(len(flag)<len(letters) and found):
    found = False
    to_find = letters[len(flag)]
    print(to_find)
    for c in chars:
        create_transaction(flag+c)
        if(read_custom()==to_find):
            flag+=c
            print(flag)
            found = True
            break
        
            

