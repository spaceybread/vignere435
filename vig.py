alphabet  = "abcdefghijklmnopqrstuvwxyz"

c = "eplxiuuynlozlrshw"

text1 = "wednesdaythursday"
text2 = "thursdaywednesday"
text3 = "wednesdaysaturday"
text4 = "saturdaywednesday"

i = 0
j = 0

texts = [text1, text2, text3, text4]


while j < 4:
    text = texts[j]
    print(text)
    i = 0
    while i < len(c):
        a = ((alphabet.index(c[i]) - alphabet.index(text[i]))%26)
        print(alphabet[a])
        i = i + 1

    j = j + 1
