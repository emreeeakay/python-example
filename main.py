# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import lesson1 as dosya

def print_hi(name = "aa"):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class emre:
    def name(self):
        print('emre')

    def surname(self):
        print('akay')

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def printData(self):
        print(self.data)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # a = input('isiminizi giriniz : ')
    # print_hi(a)

     b = Bag()
     x = ''
    # while x != 'end':
    #     x = input('bir sayı giriniz :')
    #     b.add(x)
    # else:
    #      b.printData()

    # print('lesson 1 file run: ')
    # dosya.printHelloWord()

     b.add('a')
     b.add('b')
     b.add('c')
     b.add('2')
     b.add('5')
     b.add(x)
     b.printData()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

