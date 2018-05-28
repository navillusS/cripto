import binascii

def listXOR(s):
    #All caracter from ascii is representated by a number from 0 to 255
    listTransd = []
    s = binascii.unhexlify(s)
    for i in range(256):
        de = "".join(chr(x ^ i) for x in s)
        if de.isprintable():
            listTransd.append(de)
    return listTransd


def scorePlainText(text):
    if text:
        contAscii = 0
        for i in range(65, 91):
            if chr(i) in text.upper():
                contAscii += 1
    else:
        contAscii = 0
    return contAscii

def decencripted(aX):
    aux = 0
    key = ''
    for ax in aX:
        if ax:
            contAscii = 0
            for i in range(65,91):
                if chr(i) in ax.upper():
                    contAscii += 1
            if aux < contAscii:
                key = ax
                aux = contAscii
    return key



if __name__ == '__main__':
    print(decencripted(listXOR(input())))
