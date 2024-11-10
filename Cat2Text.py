alphabet = ["a","b","c"]

def translate(data):
    data = data.lower()
    data = data.replace("meow","0").replace("mrrp", "1").replace("mreow", "2").replace("mrow", "3").replace(" ", "")
    seperatewords = data.split(";")
    finalwordlist = []
    for i in seperatewords:
        letters = [i[e:e+3] for e in range(0, len(i), 3)]
        lettersinword = []
        for x in letters:
            letternum = int(x,4)
            letter = chr(ord('`') + letternum)
            lettersinword.append(letter)
        finalwordlist.append(''.join(lettersinword))
    return ' '.join(finalwordlist)
catspeak = input("Please input the cat's words: ")
print(translate(catspeak))