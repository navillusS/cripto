import binascii

def hexTo64(hexstring):
#El dato entra como un numero hexadecimal

#Muestra el dato representado por el numero hexadecimal
    binary = binascii.unhexlify(hexstring)

#Convierte el dato en una linea de caracteres ASCII en base64 codificados
    return binascii.b2a_base64(binary)

if __name__ == '__main__':
    print(hexTo64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


