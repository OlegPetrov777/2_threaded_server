import socket
import threading

print_lock = threading.Lock()

def connection(conn, addr):
    while True:
        msg = ''
        data = conn.recv(1024)
        
        if not data:
                break
        print('Accepting data...')
        
        msg += data.decode()
        print('Sending data...')
        
        conn.send(data)
        print(f'{addr[0]} said: {msg}')

    print('Closing connection to ' + str(addr) + '...')
    conn.close()


def main():
    print('Server starting...')
    sock = socket.socket()
    sock.bind(('', 9000))
    client_num = 1

    while True:
        print('Listening to the port...')
        
        sock.listen(10)
        conn, addr = sock.accept()
        print('Connected to ' + str(addr))
        
        threading.Thread(target=connection, name="client"+str(client_num), args=[conn, addr]).start()
        client_num += 1
        
    print('Closing server...')
    sock.close()

if __name__ == '__main__':
    main()

