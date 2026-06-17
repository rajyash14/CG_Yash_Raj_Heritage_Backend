def search_word(word_list, target_word):
    for i in range(len(word_list)):
        if word_list[i] == target_word:
            return f"The word '{target_word}' is at position {i}."
    return "Word not found."

user_paragraph = input("Type a short sentence: ").split()
user_word = input("Which word do you want to find? ")
print(search_word(user_paragraph, user_word))