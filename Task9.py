def change():
    new_text = []
    text_list = list(input("Write your text: "))
    for i in text_list:
        if i.isalpha() == True or i == " ":
            new_text.append(i)
        else:
            continue
    
    # print(new_text)
    final = "".join(new_text)
    print(f"New text: {final}")
change()