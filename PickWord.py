import random

words = []
with open("sowpods.txt", "r") as fr:
    line = fr.readline()
    while line is not "":
        words.append(line)
        line = fr.readline()

def randomWord():
    return str.strip(random.choice(words))