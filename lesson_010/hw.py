# Easy A
# text = input("Введите текст: ")
# text_list = text.split()
# word_counter = len(text_list)
# print ("Количество слов в тексте: ", word_counter)


# # Easy A
# text = input()
# print(text.count(" "+1))


# # Easy B
# text = "HomeWork"
# print(text.replace("o", "$"))
# text = "Aidana"
# print(text.replace("a", "!"))
# text = "DeCode is cool"
# print(text.replace("o", "5"))

# # Medium A
# word = input("Введите слово: ")
# mid = len(word) // 2
# first_half = word[:mid]
# second_half = word[mid:]
# res = second_half + first_half
# print(res)


# Medium B
# ord - из символа в номер
# chr - из номера в символ
# text = input("Введите строку: ")
# for i in text:
#     print(ord(i), end=" ")

# Hard A
text = input("text: ")
# aplhabet = "abcedfghijklmonpqrstuvyxz"
for letter in text:
    print(letter + ":", ord(letter.lower())- 96)


# Hard B
