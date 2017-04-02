from Tkinter import *
#import sys
import socket

top=Tk()
top.title('Remote Video Car')

c=socket.socket()
host='127.0.0.1'
port=22225
c.connect((host,port))


def forward(event):
	#print ('forward')
	c.send('forward')

def backward(event):
	#print ('backward')
	c.send('backward')

def left(event):
	#print ('left')
	c.send('left')

def right(event):
	#print ('right')
	c.send("right")

def quit(event):
	#print ('quit')
	c.send('quit')
	#c.close()
	sys.exit()

def home(event):
	print('home')
	c.send('home')


Btn0 = Button(top, width=10, text='Forward')
Btn1 = Button(top, width=10, text='Backward')
Btn2 = Button(top, width=10, text='Left')
Btn3 = Button(top, width=10, text='Right')
Btn4 = Button(top, width=10,height=5,text='Quit')
Btn5 = Button(top, width=10, text='Home')

Btn0.grid(row=0,column=1)
Btn1.grid(row=2,column=1)
Btn2.grid(row=1,column=0)
Btn3.grid(row=1,column=2)
Btn4.grid(row=3,column=2)
Btn5.grid(row=1,column=1)


Btn0.bind('<ButtonPress-1>',forward)
Btn1.bind('<ButtonPress-1>',backward)
Btn2.bind('<ButtonPress-1>',left)
Btn3.bind('<ButtonPress-1>',right)
Btn4.bind('<ButtonRelease-1>',quit)
Btn5.bind('<ButtonRelease-1>',home)

top.bind('<KeyPress-w>',forward)
top.bind('<KeyPress-s>',backward)
top.bind('<KeyPress-a>',left)
top.bind('<KeyPress-d>',right)


def main():
	top.mainloop()

if __name__ == '__main__':
	main()
