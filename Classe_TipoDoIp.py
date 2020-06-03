
class Classe_do_IP:

    def tipoClasse(self, octetos):
        #print(octetos)
        if(int(octetos[0]) < 127):
            #print('Classe A')
            return 'Classe A'
        elif (int(octetos[0]) > 127 and int(octetos[0]) < 192):
            #print('Classe B')
            return 'Classe B'
        elif (int(octetos[0]) > 191 and int(octetos[0]) < 224):
            #print('Classe C')
            return 'Classe C'
        elif (int(octetos[0]) == 127):
            #print('Loopback')
            return 'Loopback'