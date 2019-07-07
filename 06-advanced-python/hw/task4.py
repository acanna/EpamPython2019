"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""
import os
import subprocess
import pytest

from task1 import PrintableFile, PrintableFolder
from task2 import Graph
from task3 import ShiftDescriptor


def test_printable_file():
    assert str(PrintableFile('file.txt')) == '-> file.txt'


@pytest.fixture()
def printable_folder_resource():
    subprocess.call(['mkdir','04-OOP'])
    subprocess.call(['mkdir', '04-OOP/hw'])
    subprocess.call(['touch', '04-OOP/OOP_1.pdf'])
    subprocess.call(['touch', '04-OOP/hw/oop_1.py'])
    subprocess.call(['touch', '04-OOP/hw/save_original_info.py'])

    yield '04-OOP'

    subprocess.call(['rm', '-r', '04-OOP'])


def test_printable_folder(printable_folder_resource):
    folder = PrintableFolder('04-OOP', os.walk('04-OOP'))
    file1 = PrintableFile('04-OOP/hw/oop_1.py')
    file2 = PrintableFile('haha.txt')

    s = '''V 04-OOP
|-> V 04-OOP/hw
|   |-> oop_1.py
|   |-> save_original_info.py
|-> OOP_1.pdf'''


    assert str(folder) == s

    assert file1 in folder
    assert file2 not in folder


@pytest.mark.parametrize('g, output', [
    ({'A': ['B'], 'B': ['C'], 'C': []}, ['A', 'B', 'C']),
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']},
     ['A', 'B', 'C', 'D']),
    ({'A': ['B', 'C', 'D'], 'B': ['C', 'D', 'E'], 'C': ['F'], 'D': ['A'],
      'E': [], 'F': []}, ['A', 'B', 'C', 'D', 'E', 'F'])
])
def test_graph_1(g, output):
    assert [v for v in Graph(g)] == output

def test_graph_2():
    g = Graph({'A': ['B'], 'B': ['C'], 'C': []})
    res = [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
            ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
    assert [(i, j) for i in g for j in g] == res

def test_sipher():
    class CeasarSipher:
        message = ShiftDescriptor(4)
        another_message = ShiftDescriptor(7)

    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
