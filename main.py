#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import time
import pyautogui

from run.run_order import run_order


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

'''

code start

- 프로그램 실행하면 order를 넣어주는 방식

--- order의 구성 ---
case 1. macro 실행
macro (macro name)

case 2. function 실행
run (function name) (function variables)

case 3. exit
exit

'''
# dir 정리
storages = {}
initial_macro = 'start_program.txt'
error_macro = 'error_program.txt'
if os.path.exists(initial_macro):
    f = open(initial_macro, "r")
    while True:
        line = f.readline().replace('\n','')
        if not line:
            print('')
            print('<<< program initiated ! >>>')
            f.close()
            break
        storages,_,_,_,_= run_order(line, storages)
if os.path.exists(error_macro):
    print('<<< error program exist >>>')

# code run
while True:
    stat = 1
    while stat:
        print('')
        order_in = input('<< Write an order >> : ')
        try:
            storages, stat ,_,_,_= run_order(order_in, storages)
        except Exception as e:
            print(str(e))        
            if os.path.exists(error_macro):
                print('')
                print('<<< error program run >>>')
                f = open(error_macro, "r")
                while True:
                    line = f.readline().replace('\n','')
                    if not line:
                        f.close()
                        break
                    storages,_,_,_,_= run_order(line, storages)
    exit_ask = input("really exit? (Y/N)")
    if exit_ask == 'Y':
        break
