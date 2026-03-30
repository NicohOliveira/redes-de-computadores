import socket
import threading as th

tam_pacote = 0 # Tamanho total dos pacotes enviados e recebidos

def enviar_msg(soquete):
    while True:
        msg = input(" -> ")
        soquete.send(msg.encode())
        if msg.lower().strip() == 'tchau':
            break

def receber_msg(soquete):
    while True:
        try:
            msg = soquete.recv(1024).decode()
            if not msg or msg.lower().strip() == 'tchau':
                break
            print(f"\nServidor: {msg}")
        except:
            break

def receber_msg(soquete):
    while True:
        msg = soquete.recv(1024).decode()
        if not msg:
            break
        print(f"\nServidor: {msg}")

def iniciar_chat(host, porta):
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((host, porta))

    thread_envio = th.Thread(target=enviar_msg, args=(soquete,))
    thread_recebimento = th.Thread(target=receber_msg, args=(soquete,))

    thread_envio.start()
    thread_recebimento.start()

    thread_envio.join()
    thread_recebimento.join()

    soquete.close()

if __name__ == '__main__':
    host = input("Digite o IP do servidor: ")
    porta = input("Digite a porta da conexao: ")

    iniciar_chat(host, int(porta))

# Trabalho 02 - em equipe: Desenvolvimento de Chat TCP/IP (Peso 2). 
# Objetivo: Criar uma aplicação em Python para tornar disponível um Chat interativo entre dois computadores via rede, 
# utilizando a arquitetura TCP/IP. Requisitos Técnicos e Documentação:
# 1) Protocolo: Utilizar a API de Socket disponível na linguagem e o protocolo TCP para a camada de transporte. 
# 2) Parametrização: A aplicação deve solicitar ao usuário (via terminal) o endereço IP de destino e a porta TCP que será 
# utilizada para fechar a conexão do Chat.TCP. 
# 3) Contabilização: Totalizar todos os pacotes enviados e recebidos, apresentando o resultado final no terminal após 
# a finalização do chat. 
# 4) Fluxograma: Apresentar uma documentação da ferramenta proposta contendo um fluxograma operacional detalhado,  
# mapeando todas as funções de envio e recebimento entre os dois computadores (lógica de cliente e servidor).
# 5) Cronograma e Regras de Entrega: Utilizar o template padrão da disciplina e enviar via e-mail para o professor, 
# respeitando rigorosamente as datas, horários e assuntos (subjects) abaixo: 
# Entrega Parcial 01: Até o dia 10/03/2026, às 10:00 horas. Assunto do e-mail: trab.lab.1s.parcial.01.chat.tcp. 
# Entrega Final:  No dia 17/03/2026, às 12:00 horas. Assunto do e-mail: trab.lab.1s.final.chat.tcp