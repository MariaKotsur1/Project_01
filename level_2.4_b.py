# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
#     pass



s = input('Введите текст : ')





def remove_last_em(s):
    
    while s[-1] == "!":
        s = s[:-1]
        
    return s

s = remove_last_em(s)
print (s)

