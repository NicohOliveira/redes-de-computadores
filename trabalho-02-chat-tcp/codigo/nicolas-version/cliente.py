import socket
import threading
import queue
from math import trunc

enviados = 0
recebidos = 0
fila = queue.Queue()
def digitar():

    while True:
        texto = input("Você: ")

        msg = {"texto": texto, "status": "na_fila"}
        fila.put(msg)
        print(f" [{texto} . . . na fila")
        if texto == "sair":
            break
def mandar(sock):
    global enviados
    while True:
        msg = fila.get()
        msg["status"] = "enviado"
        print(f"  [{msg['texto']}] -> enviando . . .")
        try:
            sock.send(msg["texto"].encode())
            msg["status"] = "enviado"
            enviados += 1
            print(f" [{msg['texto']}] -> enviado")
        except:
            break
        if msg["texto"] == "sair":
            break
def receber(sock):
    global recebidos
    while True:
        try:
            dados = sock.recv(1024)
            if not dados:
                break
            recebidos += 1
            texto = dados.decode()
            print(f"\nServidor: [{texto}]")
            print("Você: ", end="", flush=True)
            if texto == "sair":
                print("\n[Servidor saiu]")
                break
        except:
            break

def main():
    ip = input("Digite o IP do servidor: ")
    porta = int(input("Digite a porta do servidor: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, porta))
    print("Conectado com sucesso|! ! ! \n")

    t1 = threading.Thread(target=digitar)
    t2 = threading.Thread(target=mandar, args=(sock,))
    t3 = threading.Thread(target=receber, args=(sock,))

    t1.start()
    t2.start()
    t

    t1.join()
    sock.close()
    t2.join()
    t3.join()


    print(f'enviados: {enviados}')
    print(f'recebidos: {recebidos}')
if __name__ == '__main__':
    main()
