import SimpleHTTPServer
import SocketServer

address = []
port = []
giliran = 0
req = 0

for i in range(5):
	address.append('10.151.31.114')    
	port.append('21500')

for i in range(3):
	address.append('10.151.31.203')    
	port.append('21500')

for i in range(2):
	address.append('10.151.31.207')    
	port.append('21500')

for i in range(2):
	address.append('10.151.31.202')     
	port.append('21500')

for i in range(2):              
	address.append('10.151.43.74')      #atma
	port.append('21500')
    
for i in range(2):              
	address.append('10.151.43.37')      #fathi
	port.append('21500')
    
for i in range(2):              
	address.append('10.151.43.128')      #wildan
	port.append('33555')
	
class request(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		global giliran
		self.send_response(303)
		new_path = 'http://%s:%s' % (address[giliran],port[giliran])
		print new_path
        
        giliran = giliran+1
		if giliran >= len(address):
			giliran=0
		
		self.send_header('Location', new_path)
		self.end_headers()
    
'''
    def giliran_now(x):
        x = x + 1
        if x >= len(address):
            x = 0
        return x
'''
    
SocketServer.TCPServer.allow_reuse_address = True
req_handler = SocketServer.TCPServer(("", 21555), request)
print "start load balancer port %d" % (21555)
req_handler.serve_forever()
