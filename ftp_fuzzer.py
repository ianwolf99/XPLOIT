#!/usr/bin/python3
print("*****************************************************")
print("_______________*********************_________________")
print("___________*******FTP_FUZZER*********_________________")
print("________****Authored by ianwolf99****_________________")
print("******************************************************") 

import socket
#Enter the amount of junk data to fuzz e.g 5000
junk = ""

host = "192.168.43.36"
port = 21
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = socket.connect(("host",port))
banner = socket.recv(1024)
print(banner.decode())
username = "USER /;/".encode() + "anonymous /;/".encode() + "\r\n".encode()
socket.send(username)
banner2 = socket.recv(1024)
print(banner2.decode())
password = "PASS /;/".encode() + "anonymous /;/".encode() + "\r\n".encode()
banner3 = socket.recv(1024)
print(banner3.decode())
fuzz_command = "MKD /;/".encode() + bytearray(junk) +  "\r\n".encode()
socket.send(fuzz_command)
banner4 = socket.recv(1024)
print(banner4.decode())
quit_comm = "QUIT /;/".encode() +  "\r\n".encode()
socket.send(quit_comm)
socket.close()
