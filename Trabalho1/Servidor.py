import socket
import threading

semaforo = threading.Semaphore(5)
pessoas_sala = 0
lock = threading.Lock()

def iniciar_servidor():

    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor ouvindo em {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode().strip().lower() == "entrar na sala":
                        with lock:
                            if semaforo.acquire(blocking=False):
                                pessoas_sala = pessoas_sala + 1
                                resposta = f"Entrou na sala, pessoas: {pessoas_sala}"
                            else:
                                resposta = "Erro, sala cheia"
                        conn.sendall(resposta.encode())
                    elif data.decode().strip().lower() == "sair da sala":
                        with lock:
                            if pessoas_sala > 0:
                                semaforo.release()
                                pessoas_sala = pessoas_sala - 1
                                resposta = "Saiu da sala"
                            else:
                                resposta = "Erro, ninguem  na sala"
                            conn.sendall(resposta.encode())

                    else:
                        conn.sendall(b"Mensagem invalida")

if __name__ == "__main__":
    iniciar_servidor()
