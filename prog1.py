'''  Prog 6 '''
'''
text = 'My first program'
saveFile = open('program.txt','w')
saveFile.write('text')
saveFile.close()


import eg
eg.func('test')
 
'''
''' Program for socket '''

'''

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
server = 'amazon.com'
port = 80
server_ip = socket.gethostbyname(server)
print(server_ip)
'''


a = 6
b = 45
c = a + b
print(c)
