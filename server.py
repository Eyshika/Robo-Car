import socket,select,sys
s=socket.socket()
s.bind(('localhost',22225))
s.listen(10)
print socket.gethostbyname('localhost')
class method():
	def forward(self):
		print('Moving forward')

	def backward(self):
		print('Moving back')

	def left(self):
		print('Turning left')

	def right(self):
		print('Turning right')

	def quit(self):
		print('Quit control')

a=method()
inputs=[s]
while True:
	
	rs,ws,es=select.select(inputs,[],[])

	for r in rs:
		if r is s:
			c,addr=s.accept()
			print ('get connection from ', addr)
			inputs.append(c)
		else:
			try:
				data=r.recv(1024)
				
				disconnected=not data
				#sys.stdout.write(data)
				#sys.stdout.flush()
				cmd=getattr(a,data)
				cmd()
			except (socket.error,AttributeError):
				disconnected=True
			if disconnected:
				print(r.getpeername(),'disconnected')
				inputs.remove(r)
		