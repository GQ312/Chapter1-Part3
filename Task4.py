def poly_word():

    word = input("Write your word: ")
    if word[:] == word[ : : -1]:
        return f"{word} is palindrom."
    else:
        return f"{word} isn't palindrom."

print(poly_word())