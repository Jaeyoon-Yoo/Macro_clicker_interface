
import pyautogui
import keyboard
import time

def click(input_list,storages):
    x_loc = input_list[0]
    y_loc = input_list[1]
    if x_loc in storages.keys():
        x_loc = storages[x_loc]
    if y_loc in storages.keys():
        y_loc = storages[y_loc]
    pyautogui.moveTo(int(x_loc),int(y_loc))
    pyautogui.click()
    
def press_keyboard(input_list,storages):
    if len(input_list) == 1:
        if input_list[0] in storages.keys():
            input_list = storages[input_list[0]]
    for i in input_list:
        pyautogui.press(str(i))
    
def press_hotkey(input_list = ['ctrl','1']):
    pyautogui.hotkey(input_list[0],input_list[1])
    
def wait(input_list = '0.5'):
    time.sleep(float(input_list[0]))
    
def get_loc():
    print('----- mouse location detector (z : print, x : end) -----')
    mouse_loc = None
    while True:
        if keyboard.is_pressed('z'):
            mouse_loc = pyautogui.position()
            print(str(mouse_loc))
            wait('1.0')
        elif keyboard.is_pressed('x'):
            print('----- mousse location dectetor done -----')
            break
    return

def write_str(input_list, storages):
    # input_list : [var_name or str | can be multi]
    for i in input_list:
        if i in storages.keys():
            if type(storages[i]) == list:
                print(f'{i} is list...')
            else:
                pyautogui.write(str(storages[i]))
        else:
            pyautogui.write(i)