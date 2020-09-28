import socket
# http://data.pr4e.org/romeo.txt

try:
    url = input('Enter URL: ')
    host = url.split('/')[2]

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, 80))
    cmd = 'GET ' + url + 'HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    my_sock.send(cmd)

    received_data = b""

    while True:
        data = my_sock.recv(512)
        if len(data) < 1:
            break
        received_data += data

    received_data = received_data.decode()
    print(received_data[:3000])
    print(len(received_data))

    my_sock.close()

except:
    print("ERROR: The URL is improperly formatted or non-existent.")
