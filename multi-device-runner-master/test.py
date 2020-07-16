import random
list=[]
with open("test.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        list.append(line)
# a = random.choice(list)
a = random.sample(list, 10)
print(a)