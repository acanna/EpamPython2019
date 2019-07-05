"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""
import os

import pytest

from task1 import PrintableFile, PrintableFolder
from task2 import Graph
from task3 import ShiftDescriptor


def test_printable_file():
    assert str(PrintableFile('file.txt')) == '-> file.txt'


def test_printable_folder():
    folder1 = PrintableFolder('../../04-OOP', os.walk('../../04-OOP'))
    folder2 = PrintableFolder('../../05-OOP_Exceptions',
                              os.walk('../../05-OOP_Exceptions'))
    file1 = PrintableFile('../../04-OOP/hw/oop_1.py')
    file2 = PrintableFile('../../05-OOP_Exceptions/hw/oop_2.py')

    s1 = '''V ../../04-OOP
|-> V ../../04-OOP/hw
|   |-> oop_1.py
|   |-> save_original_info.py
|-> OOP_1.pdf
|-> OOP_1.pptx'''

    s2 = '''V ../../05-OOP_Exceptions
|-> V ../../05-OOP_Exceptions/hw
|   |-> counter.py
|   |-> oop_2.py
|-> Exceptions.pptx
|-> OOP_2.pptx
|-> OOP_2.pdf
|-> Exceptions.pdf'''

    assert str(folder1) == s1
    assert str(folder2) == s2

    assert file1 in folder1
    assert file2 not in folder1


@pytest.mark.parametrize('g, output', [
    ({'A': ['B'], 'B': ['C'], 'C': []}, ['A', 'B', 'C']),
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']},
     ['A', 'B', 'C', 'D']),
    ({'A': ['B', 'C', 'D'], 'B': ['C', 'D', 'E'], 'C': ['F'], 'D': ['A'],
      'E': [], 'F': []}, ['A', 'B', 'C', 'D', 'E', 'F'])
])
def test_graph(g, output):
    assert [v for v in Graph(g)] == output


def test_sipher():
    class CeasarSipher:
        message = ShiftDescriptor(4)
        another_message = ShiftDescriptor(7)

    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
