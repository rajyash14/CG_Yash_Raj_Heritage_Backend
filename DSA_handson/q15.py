def search_character(text, char_to_find):
    for i in range(len(text)):
        if text[i] == char_to_find:
            return i
    return -1

user_text = input("Enter a word or sentence: ")
user_char = input("Enter the single letter to find: ")
print(search_character(user_text, user_char))