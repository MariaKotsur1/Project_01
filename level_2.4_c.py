#Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# def remove_word_with_one_em(s):
#     pass

s = input('Введите слово - ')

def remove_word_with_one_em(s):
    new_s = list(s)
    marks = '!'
    if new_s.count(marks) == 1:
        return ' '
    else:
        return s
s = remove_word_with_one_em(s)
print(s)


                                                                                                 
