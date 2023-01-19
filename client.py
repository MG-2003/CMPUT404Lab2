import socket

BYTES_TO_READ = 4096

def get(host, port):
    # Create request
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n" #byte-array, hence pre-fxed with 'b'

    # Create our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Sent data via socket
    s.connect((host, port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)

    # listen for response
    response = s.recv(BYTES_TO_READ)
    # Exit while loop when server shutsdown wr socket
    while(len(response) > 0):
        print(response)
        response = s.recv(BYTES_TO_READ)
    
    s.close()

get("www.google.com", 80)