import tkinter
import socket, threading

win = tkinter.Tk()  # create main window
win.title('sim server')
win.geometry("400x400+200+20")
users = {} #user dictionary, can also connect database


def run(ck, ca):
    userName = ck.recv(1024) #receive message from client in the type of byte setting the unit as 1k
    users[userName.decode("utf-8")] = ck #decode and save user information
    #print(users)
    printStr = "" + userName.decode("utf-8") + "connect\n" #show whether connect successfully in the display frame.
    text.insert(tkinter.INSERT, printStr)

    while True:
        rData = ck.recv(1024) #receive message from client in the type of byte setting the unit as 1k
        dataStr = rData.decode("utf-8")
        infolist = dataStr.split(":") #split string for receiving username and message sent from server.
        users[infolist[0]].send((userName.decode("utf-8") + "says" + infolist[1]).encode("utf"))
        #send message to the object client

def start():
    ipStr = eip.get() #get ip from input side
    portStr = eport.get() #get port from input side
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket comply with ipv4 or ipv6
    server.bind((ipStr, int(portStr)))#bind ip and port number. 1. caution about the type of port number which is str, however, bind requires int type
    #2:bind() param is in the form of ()
    server.listen(10) #set listener and maximum connect number.
    printStr = "Server starts successfully\n" # whether connect successfully
    text.insert(tkinter.INSERT, printStr) #show in the information window
    while True:#sim server will keep running, therefore is a no stop looper
        ck, ca = server.accept()#receive information from connected client
        # ca is a () composed of ip and port number, ck is about client information 
        t = threading.Thread(target=run, args=(ck, ca)) #each time connect to a client, create a thread 
        # args in thread function is in the form of ()    
        t.start()#start thread 


def startSever():
    s = threading.Thread(target=start)# create a thread to open server
    s.start()#start thread

#below is the the UI
labelIp = tkinter.Label(win, text='ip').grid(row=0, column=0)
labelPort = tkinter.Label(win, text='port').grid(row=1, column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="start", command=startSever).grid(row=2, column=0)
text = tkinter.Text(win, height=5, width=30)
labeltext = tkinter.Label(win, text='connect information').grid(row=3, column=0)
text.grid(row=3, column=1)
win.mainloop()
