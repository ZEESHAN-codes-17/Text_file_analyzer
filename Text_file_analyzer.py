from collections import Counter

common = []

user = input("enter your file name: ")
with open(user, 'r') as f:
    text = f.read().lower()

    words = text.split()
    words_count = Counter(words)

    
   
    most_common = words_count.most_common(1)  # top 1
    used = {"Most frequent word": most_common[0][0], "word is: ": most_common[0][1]}
    common.append(used)
    print(common)

    lines = text.splitlines()
    print("total lines in this files are: " ,len(lines))

    word = text.split()
    print("total words in this file are: ", len(word))

    print("total characters in this file are: " ,len(text))

