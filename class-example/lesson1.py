class emre:
    ad = ''

    def printName(self):
        print('Merhaba Emre')

    def kullaniciAdi(self):
        ad = str(input('Adınızı Giriniz : '))
        print('Merhaba ' + ad)

    def zincir1(self):
        self.ad = input('adınızı Giriniz : ')
        return self

    def zincir2(self):
        if not type(self.ad) is str:
            raise TypeError("Only string are allowed")
        else:
            return self

    def zincir3(self):
        print('adınız : ' + str(self.ad))
        return self

    def zincir4(self):
        return self.zincir1().zincir2().zincir3()


class ornek:
    aa = ''

    def __init__(self):
        aa = 'asd'

    def Başlangıcda_yazdir(self):
        print(self.aa)

    def hata_yazdir(self):
        raise TypeError('Hata çıktıısıı')

if __name__ == '__main__':
    nesne = emre()
    emre.zincir4(nesne)
