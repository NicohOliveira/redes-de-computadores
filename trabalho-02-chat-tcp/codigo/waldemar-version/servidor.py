import socket
import threading as th

tam_pacote = 0 # Tamanho total dos pacotes enviados e recebidos

def enviar_msg(conex):
    while True:
        msg = input(" -> ")
        conex.send(msg.encode())            # Codifica e envia a mensagem
        if msg.lower().strip() == 'tchau':  # Se a mensagem for "tchau", encerra o envio
            break

def receber_msg(conex):
    while True:
        try:
            msg = conex.recv(1024).decode()                 # Recebe e decodifica a mensagem
            if not msg or msg.lower().strip() == 'tchau':   # Se a mensagem for nula ou "tchau", encerra o recebimento
                break
            print(f"\nCliente: {msg}")
        except:
            break

def iniciar_server(porta):
    host = '0.0.0.0' # Inicia o host local

    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.bind((host, porta))

    soquete.listen(1) 
    
    conex, endereco = soquete.accept()
    print(f"Nova conexao com: {endereco}")

    thread_envio = th.Thread(target=enviar_msg, args=(conex,))
    thread_recebimento = th.Thread(target=receber_msg, args=(conex,))

    thread_envio.start()        # Inicia a thread de envio
    thread_recebimento.start()  # Inicia a thread de recebimento 

    thread_envio.join()
    thread_recebimento.join()

    conex.close()

if __name__ == '__main__':
    porta = input("Digite a porta de entrada do servidor: ")

    iniciar_server(int(porta))