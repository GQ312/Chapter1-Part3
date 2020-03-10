# def count():
#     longest_word = ""
#     longest_size = 0
#     for word in word_list:
#         if len(word) > longest_size:
#             longest_word = word 
#             longest_size = len(word)
#     return longest_word

# words = input("Write your few words: ")
# word_list = words.split()
# print("The longest word is ",count(word_list))
# count()  


def count_word():
    text = input("Write your text: ")
    text_list = text.split(" ")
    long_words = 0
    longest = []
    for i in text_list:
        if len(i) > long_words:
            long_words = len(i)
            longest.clear()
            longest.append(i)
        else:
            continue
    
    return f"The longest word is {longest}"
print(count_word())