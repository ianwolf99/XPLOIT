#!usr/bin/python3 
print("[**********************************]")
print("[****program to print badchars*****]")
print("[*****Authored by ianwolf99********]")
print("[**********************************]")

for i in range(0,256):
    print("\\x%02x" % i,end = "")
print("\r\n[*] copy and paste the bytearray in exploit and follow the ESP in dump ")    