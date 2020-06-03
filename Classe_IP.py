# len 12 sem pontos 15 com

class IP:


    def __init__(self, ip):
        self._ip = ip

    
    def _getIP(self):
        return self._ip

    def _setIP(self, novo_ip):
        self._ip = novo_ip
        

    def contaPontos(self):
        if(self._ip.count('.') != 3):
            #print('Ip invalido')
            valido = False
            return False
        else:
            return True


    def separaOctetos(self):      
        octetos = self._ip.split('.')
        return octetos


    def verificaCampos(self, octetos):

        if(len(octetos[0]) < 4):
            if(len(octetos[1]) < 4):
                if(len(octetos[2]) < 4):
                    if(len(octetos[3]) < 4):
                        valido = True
                    else:
                        valido = False
                else:
                    valido = False
            else:
                valido = False
        else: 
            valido = False

        return valido


    def verificaOctetos(self, octetos):
        print(octetos)

ip = IP('115.221.999.626')
print(ip._getIP())

if(ip.contaPontos()):
    
    octetos = ip.separaOctetos()

    if(ip.verificaCampos(octetos)):
        ip.verificaOctetos(octetos)