import math
import HappyNumbers as hN

# primeT = open("PrimeText.txt","w")
# primeT.write(str(2) + "\n")
# primeT.write(str(3) + "\n")
# for i in range(1, 1000):
#     for j in range(2, math.ceil(i/2)):
#         if i % j is 0:
#             break
#         elif j == math.floor(i/2):
#             primeT.write(str(i) + "\n")
#             break
# primeT.close()

# happyT = open("HappyText.txt", "w")
# hapN = hN.happyNums(143)
# for i in hapN:
#     happyT.write(str(i) + "\n")
# happyT.close()

_primeR = open('PrimeText.txt')
_primeN = []
line = _primeR.readline()
while line is not '':
    _primeN.append(int(line))
    line = _primeR.readline()
_primeR.close()

hapR = open("HappyText.txt")
hapN = []
line = hapR.readline()
while line is not '':
    hapN.append(int(line))
    line = hapR.readline()
hapR.close()

intersect = []
for i in _primeN:
    for j in hapN:
        if i is j:
            intersect.append(i)

print(intersect)
