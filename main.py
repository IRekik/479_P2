import nltk
from nltk.corpus import inaugural
import os

root = os.path.abspath(os.curdir)

list_of_files = []
list_of_files.append(root + '\\reuters21578\\reut2-000.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-004.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-016.sgm')

# Subproject 1

def subproject_I_1(document):
    F = []
    new_id = 0
    trigger = 0
    for i in document:
        if trigger == 2:
            new_id = int(i)
            trigger = 0
        if trigger == 1:
            trigger = 2
        if i == "NEWID=":
            trigger = 1
        else:
            F.append((i, new_id))
    return F
def subproject_I_2(F):
    no_dup_list = set(F)
    no_dup_sorted_list = sorted(no_dup_list, key = lambda x: x[0])
    return no_dup_sorted_list

def subproject_I_3(no_dup_sorted_list):
    final_list = []
    list_of_indexes = []
    list_of_indexes.append(no_dup_sorted_list[0][1])
    final_list.append(no_dup_sorted_list[0], list_of_indexes)
    list_of_indexes.clear()
    for i in range(1, len(no_dup_sorted_list)):
        list_of_indexes.append(no_dup_sorted_list[i][1])
        if no_dup_sorted_list[i-1][0] != no_dup_sorted_list[i][0]:
            final_list.append(no_dup_sorted_list[i-1][0], list_of_indexes)
            list_of_indexes.clear()
    return final_list

for i in range(len(list_of_files)):
    document = inaugural.raw(list_of_files[i])
    tokens = nltk.word_tokenize(document)
    F = subproject_I_1(tokens)
    no_dup_sorted_list = subproject_I_2(F)
    final_list = subproject_I_3(no_dup_sorted_list)
