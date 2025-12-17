"""
Write a GPA-calculating program that reads subject scores from a file. 
The program should print each score and the corresponding grade plus the final GPA at the end.
"""

# with open('scores_paper.txt') as f:
#     read_data = f.readlines()

#     total = 0 

#     for line in read_data:
#         for char in line:
#             if char.isdigit():
#                 total += int(char)

#     print(f"{read_data} \nSum:",total)

"""
Write a program that allows the user to find how many times a word appears in a file. 
They should enter the filename and a word, and it tells them how many times the word is in that file.
"""
# file_name = input("What file to search: ")
file_name = "scores.txt"
word = "Science"
# word_to_search = input("What word to search: ")

with open(file_name, "r") as f:
    contents = f.read()
    text_count = contents.count(word)
    print("Text count:", text_count)



    # lines = f.readlines()
    # for line in lines:
    #     print(word, "String exists")
    #     print('Line Number:', lines.index(line))
    #     print('line:', line)
    #     print()

    # if word in f.read():
    #     print("True")
    
    # x = f.readlines()



    # print(x)
    
    # total = 0 

    # for line in x:
    #     # for char in line:
    #     if line.find(word_to_search):
    #             # total += 1
    #         print(line)
    
    # print(total)
    # print(x)
    # print(word_to_search)