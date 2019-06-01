""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

from collections import Counter

with open('files/rna_codon_table.txt') as f:
    table_data = f.read().split()
    codon_table = {}
    assert len(table_data) % 2 == 0
    for i in range(len(table_data) // 2):
        codon_table[table_data[2 * i]] = table_data[2 * i + 1]


def translate_from_dna_to_rna(dna):
    return dna.replace('T', 'U')


def count_nucleotides(dna):
    return sorted(list(Counter(dna).items()))


def translate_rna_to_protein(rna):
    proteins = []
    stop_index = min(rna.find('UAA'), rna.find('UAG'), rna.find('UGA'))
    protein = ''
    for i in range(stop_index % 3, len(rna) - 2, 3):
        if codon_table[rna[i:i + 3]] != 'Stop':
            protein += codon_table[rna[i:i + 3]]
        elif protein:
            proteins.append(protein)
            protein = ''

    return proteins


# read the file dna.fasta
with open('files/dna.fasta') as f:
    dna = [x[:-1] for x in f.readlines()]

starts = [i for i, x in enumerate(dna) if x.startswith('>')]
n = len(starts)
descriptions = [dna[i] for i in starts]
data = dna.copy()
for i in starts:
    data[i] = '>'
dnas = [x for x in ''.join(data).split('>') if x]
assert len(dnas) == len(starts)

# статистика по количеству нуклеотидов в ДНК
with open('files/dna.stats', 'w') as f:
    for i in range(n):
        f.write(descriptions[i] + '\n')
        f.write(str(count_nucleotides(dnas[i])) + '\n')

# последовательность РНК для каждого гена
with open('files/dna.rna', 'w') as f:
    for line in dna:
        if line.startswith('>'):
            f.write(line + '\n')
        else:
            f.write(translate_from_dna_to_rna(line) + '\n')

# последовательность кодонов для каждого гена
with open('files/dna.codon', 'w') as f:
    for i in range(n):
        f.write(descriptions[i] + '\n')
        f.write('\n'.join(translate_rna_to_protein(
            translate_from_dna_to_rna(dnas[i]))) + '\n')
