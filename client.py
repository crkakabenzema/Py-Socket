import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("client2")
win.geometry("400x400+200+20")

ck = None #for saving client information


def getInfo():
    while True:
        data = ck.recv(1024)#for receiving message from server
        text.insert(tkinter.INSERT, data.decode("utf-8"))#show in the information frame 


def connectServer():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket comply with ipv4 and ipv6
    client.connect((ipStr, int(portStr)))#connect ip and port number.
    1.cautious about input port number is in the type of str. however, it requires int type
    2.bind() param is in the type of () 
    client.send(userStr.encode("utf-8"))
    ck = client

    t = threading.Thread(target=getInfo)
    t.start()


def sendMail():
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr
    ck.send(sendStr.encode("utf-8"))


#below is UI
labelUse = tkinter.Label(win, text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
eport = tkinter.Variable()

entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="start", command=connectServer).grid(row=3, column=0)
text = tkinter.Text(win, height=5, width=30)
labeltext= tkinter.Label(win, text="show message").grid(row=4, column=0)
text.grid(row=4, column=1)

esend = tkinter.Variable()
labelesend = tkinter.Label(win, text="sent message").grid(row=5, column=0)
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
labelefriend= tkinter.Label(win, text="send to").grid(row=6, column=0)
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win, text="send", command=sendMail).grid(row=7, column=0)
win.mainloop()
