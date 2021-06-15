
# from random import randint
# dice1 = []
# dice2 = []

# print('   ..::Welcom to The Rolling Dices::..')

# def roll():
#     num = randint(1,6)
#     return num

# def duplicates(l1, l2):
#     matches= [i for i, j in zip(l1, l2) if i == j]
#     return matches
# # print result with counters

# while True:
#     choose =input("Enter 'Y' to roll a dice. 'E' to exit the game :")
#     if choose.upper() == 'E':
#             break
#     if choose.upper() == 'Y':
#         n = int(input('Enter how many times to roll the dices(1-100):'))
#         if n <0 or n > 100: 
#             print('Wrong! the number is not valid!')
#             continue
#         else:
#             for i in range(n):
#                 dice1.append(roll())
#                 dice2.append(roll())
#                 print(i+1,"-", "rolling:", dice1[i], dice2[i])
                
#     matches = duplicates(dice1, dice2) 
     
#     for i in matches:
#         if matches.count(i)==1:
#             print("Number",i,i,"came out:", 1, "times")
#         elif matches.count(i)>1:
#             print("Number",i,i,"came out:", matches.count(i), "times")
 

import random

class Lotto:

    def __init__(self, name):
        self.name= name
       
    def play(self, number):
        lottos=[]
        self.number = number
        c=0
        while c<number:
            num = (random.randint(1,36))
            if num in lottos:
                continue
            lottos.append(num)
            c+=1
        return lottos
               

lotto1 = Lotto('Swedish')
f = lotto1.play(7)
f.sort()
print("The result for", lotto1.name, "is:", f)