import socket

def iniciar_Cliente():

    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))

        S.sendall(b"bom dia")
        data = S.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

        S.sendall(b"data e hora")
        data = S.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

        S.sendall(b"fatorial")
        data = S.recv(1024)
        if data.decode() == "número":
            S.sendall(b"7")
            data = S.recv(1024)
            print(f"Resposta: {data.decode()}")

        S.sendall(b"fibo")
        data = S.recv(1024)
        if data.decode() == "número":
            S.sendall(b"3")
            data = S.recv(1024)
            print(f"Resposta: {data.decode()}")

if __name__ == "__main__":
    iniciar_Cliente()