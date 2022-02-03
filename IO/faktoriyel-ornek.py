if __name__ == '__main__':
    a = int(input('Faktoriyeli alınıcak sayıyı giriniz : ')) # burada input ile girilen verinin integer türüne cevap vermekte
    b = 1
    for i in range(1, a + 1):
        b = b * i

    print('sonuc :' + str(b))


def fakt(x):
    return 1\
        if (x == 1 or x == 0)\
        else x * fakt(x - 1)

sayi = int(input('Lütfen Faktöriyelini Hesaplamak İstediğini Sayını Giriniz : '))
print(str(sayi) + " Sayısının faktöriyeli  =  " + str(fakt(sayi)))