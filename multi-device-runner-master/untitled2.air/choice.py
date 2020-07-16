import random

def get_num():
    list=[]
    with open("test.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            list.append(line)
    a = random.choice(list)
    return a