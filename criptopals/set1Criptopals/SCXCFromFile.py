from singleCharXorCipher import listXOR, decencripted
def scxcf(s):
    i = 1
    with open(s) as file:
        lines_read = file.readlines()
        for line in lines_read:
            #print(line)
            print(decencripted(listXOR(line[:-1])))
            print('/**************************'+ str(i)+'***********************/\n\n')
            i += 1

if __name__ == '__main__':
    scxcf("/home/navillus/Downloads/4.txt")