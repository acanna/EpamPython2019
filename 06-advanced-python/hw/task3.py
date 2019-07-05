"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""
import time


class ShiftDescriptor:

    def __init__(self, n):
        self.shift = n
        self.label = str(time.time())

    def __get__(self, instance, owner):
        return ''.join(list(map(lambda s: chr(ord(s) + self.shift),
                                getattr(instance, self.label))))

    def __set__(self, instance, value):
        setattr(instance, self.label, value)


class CeasarSipher:
    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'

assert a.message == 'efg', a.message
assert a.another_message == 'olssv', a.another_message
