import binascii
a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
a = int(a, 16)
b = int(b, 16)

xor = a ^ b

print(hex(xor))



#if __name__ == '__main__':
