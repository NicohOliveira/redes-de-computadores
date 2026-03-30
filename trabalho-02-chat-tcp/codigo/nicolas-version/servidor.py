import socket
import threading
import queue

enviados = 0
recebidos = 0

fila = queue.Queue()

def digitar():
    global enviados
    while True:
        texto= input("voce : ")
        msg = {"texto": texto, "status": "na_fila"}
        fila.put(msg)
        print(f"  [{texto}] na fila. . .")
        if texto == "sair":
            break
def mandar(conn):
    global enviados
    while True:
        msg = fila.get()
        msg ["status"] = "enviando"
        print(f"[{msg['texto']}] -> enviando patrick. . .")
        try:
            conn.send(msg["texto"].encode())
            msg["status"] = "enviado patrtick"
            enviados += 1
            print(f"  [{msg['texto']}] -> enviado patrick! !")
        except:
            break
        if msg["texto"] == "sair":
            break
def receber(conn):
    global recebidos
    while True:
        try:
            dados = conn.recv(1024)
            if not dados:
              break
            recebidos+=1
            texto = dados.decode()
            print(f"\nCliente: [{texto}]")
            print("Você: ", end="", flush=True)
            if texto == "sair":
                print("[\nCliente saiu!")
                break

        except:
            break

def main():
    porta =int(input("digite a porta do servidor"))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", porta))
    s.listen(1)
    print(f"socket ouvindo na porta {porta}. . .")
    conn, addr = s.accept()

    t1 = threading.Thread(target=digitar)
    t2 = threading.Thread(target=mandar, args=(conn,))
    t3 = threading.Thread(target=receber, args=(conn,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    conn.close()
    s.close()
    print(f"Enviados:{enviados}")
    print(f"Recebidos:{recebidos}")

if __name__ == '__main__':
    main()
