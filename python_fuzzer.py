import socket

buffer = ["A"]
counter = 50

while len(buffer) <= 1000:
    buffer.append("A" * counter)
    counter = counter + 50

for buffstring in buffer:
    print "Fuzzing:" + str(len(buffstring))
    request =  "GET https://facebook.com HTTP/1.0\r\n"                                                                                       Host: facebook.com
	request += "User-Agent: squidclient/3.5.28\r\n"
	request += "Accept: */*\r\n"
	request += "Proxy-Authorization: Basic c3F1aWQ6c3F1aWQ=\r\n"
	request += "Connection: close\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( ("127.0.0.1", 3128) )
    sock.send(request)
    res = sock.recv(1024)
    print(res)
    #sock.send(buffstring)
    sock.close()
    

