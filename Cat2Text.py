from base4 import encode


def cat2text(data):
    data = data.lower()
    data = data.replace("meow", "0").replace("mrrp", "1").replace(
        "mreow", "2").replace("mrow", "3").replace(" ", "")
    seperatewords = data.split(";")
    finalwordlist = []
    for i in seperatewords:
        letters = [i[e:e+3] for e in range(0, len(i), 3)]
        lettersinword = []
        for x in letters:
            letternum = int(x, 4)
            letter = chr(ord('`') + letternum)
            lettersinword.append(letter)
        finalwordlist.append(''.join(lettersinword))
    return ' '.join(finalwordlist)


def text2cat(data):
    data = data.lower()
    words = [word for word in data.split(" ")]
    output = ''
    for word in words:
        new_word = ''
        for letter in word:
            num = ord(letter) - 96
            # add leading zeros
            encoded = format(f'{int(encode(num)):03d}')
            encoded = encoded.replace("0", "meow ",).replace("1", "mrrp ").replace(
                "2", "mreow ").replace("3", "mrow ")
            new_word += encoded

        new_word = new_word.strip()
        new_word += '; '
        output += new_word

    output = output[:-2]

    return output


print("Pick your translation:")
print("1) cat to text")
print("2) text to cat")

selection = cat2text if int(input()) == 1 else text2cat
catspeak = input("Please input the words: ")
print(selection(catspeak))
