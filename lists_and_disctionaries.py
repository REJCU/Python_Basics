"""
Let's see if you can cheat on multiple-choice exams... 
Write a program to determine which answers appear most frequently (a, b, c, d...). 
The tutorial solutions contain some multiple-choice answers, so store these in a text file, 
then write a program that prints the answers (sorted) and how frequently they occur.
E.g. it might print: B: 13, C: 12, D: 9, A: 4
"""
# import random

# storage = {}

# with open( "random_scores.txt", "w") as f:
#     for x in range(100):
#         line = random.choices(answers)
#         f.write(str(line))

# with open("random_scores.txt", "r") as f:
#         contents = f.read().upper().strip()
        
#         only_letters = [content.strip().upper() for content in contents if content.isalpha()]
        
#         for answer in only_letters:
#             storage[answer] = storage.get(answer, 0) + 1 
#             sorted_results = sorted(storage.items(), key=lambda item: item[1], reverse=True)
            

#         for letter, count in sorted_results:
#             print(f"{letter}: {count}")
        

# Filters out anything that isn't a letter
# only_letters = [char.upper() for char in clean_answers if char.isalpha()]
            # This sorts the dictionary items by their value (the count) in reverse order
# sorted_results = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# for letter, count in sorted_results:
#     print(f"{letter}: {count}")

        # x = [x for x in contents if "A" in x]
        # print(set(x.count()))
        # print(len(x))
        # print(len(contents))
        # print(x)
        # print(contents)


# for answer in data:
#     counts[answer] = counts.get(answer, 0) + 1
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# Source - https://stackoverflow.com/a
# Posted by newacct
# Retrieved 2025-12-18, License - CC BY-SA 2.5

# def most_common(lst):
#     return max(set(lst), key=lst.count)


# with open(file_name, "r") as f:
#     contents = f.read()
#     text_count = contents.count(word)
#     print("Text count:", text_count)


"""
Modify the word-counting program (from File I/O) 
so that the user can enter an arbitrary number of words and it prints the number of times each of those words occurs
"""

word_store = {}

file_name = "scores.txt"
word = input("Enter a words: ")

with open( "random_words.txt", "w") as f:
        f.write(word)

with open("random_words.txt", "r") as rwords:
    contents = rwords.read().split()
    word_count = contents.count(word)
    print("Word count: ", word_count, contents)

    only_words = [content.strip().lower() for content in contents]
    print("Only words: ", only_words)

    for answer in only_words:
        word_store[answer] = word_store.get(answer, 0) + 1
        print("Answer: ", answer, word_store[answer])

#         only_letters = [content.strip().upper() for content in contents if content.isalpha()]

        # for answer in only_letters:
        #     storage[answer] = storage.get(answer, 0) + 1
        #     sorted_results = sorted(storage.items(), key=lambda item: item[1], reverse=True)


#         for letter, count in sorted_results:
#             print(f"{letter}: {count}")