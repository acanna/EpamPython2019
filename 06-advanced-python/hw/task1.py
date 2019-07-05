"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import os


class PrintableFolder:
    def __init__(self, name, content):
        if len(name) > 1 and name.endswith('/'):
            name = name[:-1]
        self.name = name
        self.content = list(content)

    def __str__(self):
        assert self.content, (self.name, self.content, os.walk(self.name))
        res = [f'V {self.name}']
        if self.content[0][1]:
            for folder in self.content[0][1]:
                folder_path = f'{self.name}/{folder}'
                res.append('|-> ' + '|   '.join(
                    str(PrintableFolder(folder_path,
                                        os.walk(folder_path))).splitlines(
                        keepends=True)))
        if self.content[0][2]:
            for file in self.content[0][2]:
                res.append(f'|{str(PrintableFile(file))}')
        return '\n'.join(res)

    def __contains__(self, item):
        return os.path.abspath(item.name).startswith(
            os.path.abspath(self.name))


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'-> {self.name}'
