def count_():
    letters = 0
    text = input("Write your text: ")
    text1 = text.strip(" ")
    text_for_str = list(text)
    for i in text_for_str:
        if i != " ":
            letters += 1
        else:
            continue
    

    print(f"Count of words: {text1.count(' ') + 1}")
    print(f"Count of letters: {letters}")
    print(f"Count of strings: {((len(text_for_str) + 16) // 80) + 1}")
    
count_()