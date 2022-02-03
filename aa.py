
class hesap:
    def topla(self, num1, num2):
        print( num1 +num2)

    def cikar(self, num1 , num2):
        print( num1 - num2)

if __name__ == '__main__':
    num1 = int(input('ilk sayıyı giriniz : '))
    num2 = int(input('ikinci sayıyı giriniz  : '))
    islem = str(input('yapak isteginiz işlem : '))
    h = hesap()

    if islem == "topla":
        h.topla(num1, num2)

    if islem == 'cikar' :
        h.cikar(num2= num2, num1= num1)

