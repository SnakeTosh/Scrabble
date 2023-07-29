import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dico = {"e": 1, "a": 1, "i": 1, "o": 1, "n": 1, "r": 1, "t": 1, "l": 1, "s": 1, "u": 1, "d": 2, "g": 2, "b": 3, "c": 3, "m": 3, "p": 3, "f": 4, "h": 4, "v": 4, "w": 4, "y": 4, "k": 5, "j": 8, "x": 8, "q": 10, "z": 10}

n = int(input())
liste=[]
for i in range(n):
    w = input()
    liste.append(w)
letters = input()

split = []

for i in letters:
    split.append(i)

valid_word = []
for word in liste:
    len_word = len(word)
    tour = 0
    for i in word:
        if i in split :
            drop = i
            tour +=1
            for i in split:
                if i==drop:
                    split.remove(i)
                    break
        else:
            if len(split) != len(letters):
                split.clear()
                for i in letters:
                    split.append(i)
            break

        if tour == len_word:
            valid_word.append(word)
            split.clear()
            for i in letters:
                split.append(i)
            break

valeur_word = []
laps = 0

for word in valid_word:
    valeur = 0
    tour = 0
    len_word = len(valid_word[laps])
    for i in word:
        tour +=1
        valeur += dico[i]
        if tour == len_word:
            valeur_word.append(valeur)
    laps +=1


index = 0
rep = index
bigger = 0
if len(valid_word) >1:

    for i in valeur_word:
        if i > bigger :
            bigger = i
            rep = index
        index +=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(valid_word[rep])