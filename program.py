import socket
import time
import threading 
from tkinter import *
root=Tk()
root.geometry("300x500")
root.config(background="white")
def func ():
    t= threading.Thread(target=recv)
    t.start()
def recv():
    listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=3050 #must be the same as the sending port number
    maxconnection=99
    ip=socket.gethostname()
    print(ip)

    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,adress)=listensocket.accept()

    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=='':
            time.sleep(5)
            lstbx.insert(0,"Client: "+sendermessage)
xr=0
def sendmsg():
    global xr,s
    if xr==0:
        s=socket.socket()
        hostname="DESKTOP-7C41EV3"
        port=4050
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbx.insert(0,"You: "+msg)
        s.send(msg.encode())
        xr+=1
    else:
        msg=messagebox.get()
        lstbx.insert(0,"You: "+msg)
        s.send(msg.encode())

def threadsendmsg():
   th = threading.Thread(target=sendmsg)
   th.start()
   
startchatimage=PhotoImage(file='start.png').subsample(4,4)
buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
buttons.place(x=130,y=10)

message = StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessageimg=PhotoImage(file='send.png').subsample(20,20 )

sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)
lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)
root.mainloop()