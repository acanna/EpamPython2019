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

# read the file dna.fasta
with open('files/dna.fasta') as f:
    dna = [x[:-1] for x in f.readlines()]

starts = [i for i, x in enumerate(dna) if x.startswith('>')]
descriptions = [dna[i] for i in starts]
for i in starts:
    dna[i] = '>'
dnas = [x for x in ''.join(dna).split('>') if x]
assert len(dnas)==len(starts)


with open('files/dna.stats', 'w') as f:
    for i, x in enumerate(starts):
        f.write(descriptions[i] + '\n')
        f.write(str(list(Counter(dnas[i]).items()))+'\n')



def translate_from_dna_to_rna(dna):
    
    """your code here"""
    pass
    # return rna


def count_nucleotides(dna):
    
    """your code here"""
    
    # return num_of_nucleotides


def translate_rna_to_protein(rna):
    
    """your code here"""
    
    # return protein
