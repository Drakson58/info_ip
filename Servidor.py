import socket
from Classe_IP import IP


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
porta = 9981
servidor.bind((host, porta))
servidor.listen(5)


while True:

    
    conexaoCliente, ipCliente = servidor.accept()

    while True:

        # Recebendo msg do cliente
        string = conexaoCliente.recv(1024)
        mensagem = string.decode('ascii')
        
        if(mensagem == 'fechar'):

            print('Conexão fechada.')
            conexaoCliente.close()
            break
        else:

            ip = IP(mensagem)
            if(ip.contaPontos()):
                octetos = ip.separaOctetos()
                if(ip.verificaCampos(octetos)):
                    if(ip.verificaOctetos(octetos)):      
                        if(ip.verificaNumeros(octetos)):                          
                            dado = ip.tipoClasse(octetos)

                            # Enviando msg pro cliente
                            msg = dado.encode('ascii')
                            conexaoCliente.send(msg)
    
    
        



