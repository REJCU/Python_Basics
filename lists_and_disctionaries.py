"""
Let's see if you can cheat on multiple-choice exams... 
Write a program to determine which answers appear most frequently (a, b, c, d...). 
The tutorial solutions contain some multiple-choice answers, so store these in a text file, 
then write a program that prints the answers (sorted) and how frequently they occur.
E.g. it might print: B: 13, C: 12, D: 9, A: 4
"""
import random

answers = ["a","b","c","d"]


with open( "random_scores.txt", "w") as f:
    for x in range(100):
        line = random.choices(answers)
        f.write(str(line))

