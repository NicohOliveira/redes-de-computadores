# Trabalho 02: Chat Interativo TCP/IP

## Enunciado

Desenvolver uma aplicação de chat interativo entre dois computadores utilizando a arquitetura TCP/IP em Python, através da API de sockets, permitindo comunicação bidirecional entre cliente e servidor.

O sistema deve permitir parametrização de conexão, contabilização de pacotes enviados e recebidos e documentação do fluxo operacional.

---

## Requisitos atendidos

* [x] 01 - Comunicação via protocolo TCP (Sockets)
* [x] 02 - Parametrização de IP e Porta via terminal
* [x] 03 - Envio e recebimento simultâneo (Threads)
* [x] 04 - Contabilização de mensagens enviadas
* [x] 05 - Contabilização de mensagens recebidas
* [x] 06 - Fluxograma operacional documentado

---

## Estrutura do Projeto

```
codigo/
├── cliente.py
└── servidor.py
```

---

## Como executar

⚠️ Execute em **dois terminais** ou em **dois computadores na mesma rede**.

### Terminal 1 — Servidor (aguarda conexão)

```bash
cd codigo
python servidor.py
```

Digite a porta desejada:

```
digite a porta do servidor: 5000
```

---

### Terminal 2 — Cliente (conecta ao servidor)

```bash
cd codigo
python cliente.py
```

Informe:

```
Digite o IP do servidor: 127.0.0.1
Digite a porta do servidor: 5000
```

---

## Funcionamento

* O servidor inicia um socket TCP e aguarda conexões.
* O cliente estabelece conexão informando IP e porta.
* O envio e recebimento ocorrem simultaneamente através de **threads**:

  * Thread de digitação
  * Thread de envio
  * Thread de recebimento
* As mensagens são armazenadas em fila antes do envio.
* Ao digitar `sair`, a conexão é encerrada.

---

## Contabilização

Ao finalizar o chat, o sistema apresenta:

```
Enviados: X
Recebidos: Y
```

Indicando o total de mensagens trocadas durante a sessão.

---

## Tecnologias utilizadas

* Python 3
* Socket API
* TCP/IP
* Threading
* Queue (fila de mensagens)

---

## Autor(es)

* Nicolas Henrique Lima de Oliveira
* Waldemar Serafim Neto
Disciplina: Rede de Computadores
Ano/Semestre: 2026/1
