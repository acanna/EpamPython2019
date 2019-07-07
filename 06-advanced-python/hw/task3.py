"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""
import time


class ShiftDescriptor:

    def __init__(self, n):
        self.shift = n

    def __get__(self, instance, owner):
        return ''.join(list(map(lambda s: chr(ord(s) + self.shift),
                                self.value)))

    def __set__(self, instance, value):
        self.value = value


class CeasarSipher:
    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'

assert a.message == 'efg', a.message
assert a.another_message == 'olssv', a.another_message
