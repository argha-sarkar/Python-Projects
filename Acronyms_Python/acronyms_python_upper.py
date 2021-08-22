phrase_input = str(input("Enter a Phrase: "))
txt = phrase_input.split()
word = " "
for i in txt:
    word = word + str(i[0]).upper()
print(word)
