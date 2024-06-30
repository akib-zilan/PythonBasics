print("Enter a sentence : ")
sentence = input()

word_list = sentence.split()

for word in word_list : 
    word_list_lowercase = list(map(lambda word: word.lower(), word_list))

print(word_list_lowercase)

word_count = {}

for w in word_list_lowercase :
    if w in word_count :
        word_count[w] +=1
    else :
        word_count[w] = 1

print(word_count)