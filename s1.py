import socket
import os
import sys

#inisialisasi alamat
#address = socket.gethostbyname(socket.gethostname())
#port = int(sys.argv[1])
#address = socket.gethostname()
#port = 21500
server_addr = ('10.151.43.179',21500);
num = 0
#mulai set koneksi
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_addr)
sock.listen(30000)

print '%s : %s'%server_addr

gambar1 = open("gambar.jpg","rb")
index = gambar1.read()
gambar1.close()

#tangkap koneksi`
try:
    while True:
        client_con,client_addr=sock.accept()
        num = num+1
        print num
        request = client_con.recv(2048)	
        request_data=request.split()
        
        
        if len(request_data) > 1:
            temp = request_data[1]
        else:
            temp = "/"
                
        try:
            data_send = "HTTP/1.1 200 OK \r\n\r\n%s"%index
            client_con.sendall(data_send)
        except:
            err="HTTP/1.1 404 Not Found\r\n\r\n <h1>NOT FOUND</h1>"
            client_con.sendall(err)
            print 'gagal'
        client_con.close()
except KeyboardInterrupt:
	print 'Server Disconnect'
	exit(0)
            
        
