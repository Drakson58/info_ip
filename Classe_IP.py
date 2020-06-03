
class IP:


    def __init__(self, ip):
        self._ip = ip

    
    def _getIP(self):
        return self._ip

    def _setIP(self, novo_ip):
        self._ip = novo_ip
        
    def _getValidado(self):
        return self.__validado


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
        if(octetos[0].isdigit()):
            if(octetos[1].isdigit()):
                if(octetos[2].isdigit()):
                    if(octetos[3].isdigit()):
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


    def verificaNumeros(self, octetos):
        if(int(octetos[0]) < 256):
            if(int(octetos[1]) < 256):
                if(int(octetos[2]) < 256):
                    if(int(octetos[3]) < 256):
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


ip = IP('127.0.0.1')
print(ip._getIP())

if(ip.contaPontos()):

    octetos = ip.separaOctetos()
    if(ip.verificaCampos(octetos)):
        if(ip.verificaOctetos(octetos)):
            if(ip.verificaNumeros(octetos)):
                print('É um ip')
                