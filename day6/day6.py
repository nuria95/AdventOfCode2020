import numpy as np

data = open("input").read().split("\n\n")

def countAnyYes():
    nums_yes = 0
    for answer_group in data:
        a = set(answer_group) # unique elements of all group answers
        a.discard('\n')
        nums_yes += len(a)
    return nums_yes

print('Num yes Day 6.1:', countAnyYes())

def createPersonSets(data):
    for n in data.split('\n'):
        yield set(n)


def countAllYes():
    nums_yes = 0
    for answer_group in data:
        a = [i for i in createPersonSets(answer_group)]
        nums_yes += len(a[0].intersection(*a[1:]))
    return nums_yes


print('Num yes Day6.2:', countAllYes())
