import nltk
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.porter import *
import os
import copy

root = os.path.abspath(os.curdir)

list_of_files = [root + '\\reuters21578\\reut2-000.sgm', root + '\\reuters21578\\reut2-004.sgm',
                 root + '\\reuters21578\\reut2-016.sgm']


# Subproject 1


def subproject_I_1(document):
    F = []
    new_id = 0
    trigger = 0
    for i in document:
        if trigger == 1 and i.isnumeric():
            new_id = int(i)
            trigger = 0
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
    list_of_indexes = [no_dup_sorted_list[0][1]]
    final_list.append(tuple((no_dup_sorted_list[0], list_of_indexes)))
    list_of_indexes.clear()
    for x in range(1, len(no_dup_sorted_list)):
        list_of_indexes.append(no_dup_sorted_list[x][1])
        if no_dup_sorted_list[x-1][0] != no_dup_sorted_list[x][0]:
            final_list.append(tuple([no_dup_sorted_list[x-1][0], copy.deepcopy(list_of_indexes)]))
            list_of_indexes.clear()
    # print(final_list)
    return final_list

print("===================")
print("SUBPROJECT I")
print("===================")
count = 1
for i in range(len(list_of_files)):
    print('FILE #' + str(count))
    document = inaugural.raw(list_of_files[i])
    tokens = nltk.word_tokenize(document)
    pairer = subproject_I_1(tokens)
    n_d_s_l = subproject_I_2(pairer)
    answer = subproject_I_3(n_d_s_l)
    count += 1


# Subproject 2

list_of_files.clear()
list_of_files.append(root + '\\reuters21578\\reut2-000.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-001.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-002.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-003.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-004.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-005.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-006.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-007.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-008.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-009.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-010.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-011.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-012.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-013.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-014.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-015.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-016.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-017.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-018.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-019.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-020.sgm')
list_of_files.append(root + '\\reuters21578\\reut2-021.sgm')


def subproject_II_1(list_of_words):
    c = 0
    for j in list_of_files:
        f = inaugural.raw(list_of_files[c])
        t = nltk.word_tokenize(f)
        p = subproject_I_1(t)
        l = subproject_I_2(p)
        a = subproject_I_3(l)
        for k in a:
            if k[0] in list_of_words:
                print("In document " + str(j) + ', the word ' + str(k[0]) + ' has been found at the DocIDs ' + str(k[1]))
        c = c + 1


def subproject_II_2():
    challenge_queries = ['copper', 'Samjens', 'Carmark', 'Bundesbank']
    subproject_II_1(challenge_queries)

print("===================")
print("SUBPROJECT 2")
print("===================")
# subproject_II_2()


# Subproject 3

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def subproject_III_1():
    total_unfiltered_distinct = 0
    total_unfiltered_nonpositional = 0
    total_unfiltered_tokens = 0
    total_nonumber_distinct = 0
    total_nonumber_nonpositional = 0
    total_nonumber_tokens = 0
    total_lowercase_distinct = 0
    total_lowercase_nondisposal = 0
    total_lowercase_tokens = 0
    total_stopword_distinct = 0
    total_stopword_nondisposal = 0
    total_stopword_tokens = 0
    total_porter_distinct = 0
    total_porter_nondisposal = 0
    total_porter_tokens = 0
    for s in range(len(list_of_files)):
        f = inaugural.raw(list_of_files[s])
        t = nltk.word_tokenize(f)
        np = subproject_I_3(subproject_I_2(subproject_I_1(t)))
        d = subproject_I_3(subproject_I_2(subproject_I_1(t)))
        unfiltered_distinct = len(d)
        unfiltered_nonpositional = 0
        for item1 in range(len(np)):
            unfiltered_nonpositional = unfiltered_nonpositional + len(np[item1][1])
        unfiltered_tokens = len(t)
        n_t = []
        n_n = []
        n_d = []
        for v1 in t:
            if not containsNumber(v1):
                n_t.append(v1)
        n_n = subproject_I_3(subproject_I_2(subproject_I_1(n_t)))
        n_d = subproject_I_3(subproject_I_2(subproject_I_1(n_t)))
        nonumber_distinct = len(n_d)
        nonumber_nonpropostional = 0
        for item2 in range(len(n_n)):
            nonumber_nonpropostional = nonumber_nonpropostional + len(n_n[item2][1])
        nonumber_tokens = len(n_t)
        l_t = []
        l_n = []
        l_d = []
        for v2 in n_t:
            if v2.islower():
                l_t.append(v2)
        l_n = subproject_I_3(subproject_I_2(subproject_I_1(l_t)))
        l_d = subproject_I_3(subproject_I_2(subproject_I_1(l_t)))
        lowercase_distinct = len(l_d)
        lowercase_nonpropositional = 0
        for item3 in range(len(l_n)):
            lowercase_nonpropositional = lowercase_nonpropositional + len(l_n[item3][1])
        lowercase_tokens = len(l_t)
        s_t = []
        s_n = []
        s_d = []
        for word in l_t:
            if not word in stopwords.words('english'):
                print(word)
                s_t.append(word)
        # s_t = [word for word in l_t if not word in stopwords.words()]
        s_n = subproject_I_3(subproject_I_2(subproject_I_1(l_t)))
        s_d = subproject_I_3(subproject_I_2(subproject_I_1(l_t)))
        stopword_distinct = len(s_d)
        stopword_nonpropositional = 0
        print('nyess')
        for item4 in range(len(s_n)):
            stopword_nonpropositional = stopword_nonpropositional + len(s_n[item4][1])
        stopword_tokens = len(s_t)
        p_t = []
        p_n = []
        p_d = []
        object = PorterStemmer()
        p_t = [object.stem(b) for b in s_t]
        p_n = subproject_I_3(subproject_I_2(subproject_I_1(p_t)))
        p_d = subproject_I_3(subproject_I_2(subproject_I_1(p_t)))
        porter_distinct = len(p_d)
        porter_nonpropositional = 0
        for item5 in range(len(p_n)):
            porter_nonpropositional = porter_nonpropositional + len(p_n[item5][1])
        porter_tokens = len(p_t)
        total_unfiltered_distinct = total_unfiltered_distinct + unfiltered_distinct
        total_unfiltered_nonpositional = total_unfiltered_nonpositional + unfiltered_nonpositional
        total_unfiltered_tokens = total_unfiltered_tokens + unfiltered_tokens
        total_nonumber_distinct = total_nonumber_distinct + nonumber_distinct
        total_nonumber_nonpositional = total_nonumber_nonpositional + nonumber_nonpropostional
        total_nonumber_tokens = total_nonumber_tokens + nonumber_tokens
        total_lowercase_distinct = total_lowercase_distinct + lowercase_distinct
        total_lowercase_nondisposal = total_lowercase_nondisposal + lowercase_nonpropositional
        total_lowercase_tokens = total_lowercase_tokens + lowercase_tokens
        total_stopword_distinct = total_stopword_distinct + stopword_distinct
        total_stopword_nondisposal = total_stopword_nondisposal + stopword_nonpropositional
        total_stopword_tokens = total_stopword_tokens + stopword_tokens
        total_porter_distinct = total_porter_distinct + porter_distinct
        total_porter_nondisposal = total_porter_nondisposal + porter_nonpropositional
        total_porter_tokens = total_porter_tokens + porter_tokens
    print("Unfiltered")
    print(total_unfiltered_distinct)
    print(total_unfiltered_nonpositional)
    print(total_unfiltered_tokens)
    print("No number")
    print(total_nonumber_distinct)
    print(total_nonumber_nonpositional)
    print(total_nonumber_tokens)
    print("No lowercase")
    print(total_lowercase_distinct)
    print(total_lowercase_nondisposal)
    print(total_lowercase_tokens)
    print("No stop words")
    print(total_stopword_distinct)
    print(total_stopword_nondisposal)
    print(total_stopword_tokens)
    print("Post Porter Stemming")
    print(total_porter_distinct)
    print(total_porter_nondisposal)
    print(total_porter_tokens)


print("===================")
print("SUBPROJECT 3")
print("===================")

subproject_III_1()