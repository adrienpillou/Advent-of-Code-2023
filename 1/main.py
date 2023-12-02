import re

with open("in.txt", 'r') as file:
    x = file.read()
    x = x.split("\n")
s = 0
digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
words_digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
values = list()

for i, v in enumerate(x):
    code = v
    word_occurences_queue = list()

    # Cas ou le premier et le dernier caractère d'un mot sont des chiffres
    if code[0].isdigit() and code[-1].isdigit():
        values.append(int(code[0] + code[-1]))
        continue

    # Trouver toutes les occurences de chiffres dans le mot
    digits_occurences = []
    for i, c in enumerate(code):
        if c.isdigit():
            digits_occurences.append([c, i])

    # Trouver toutes les occurences de chiffres en lettres dans le mot
    for w in words_digits_list:
        occurences = [m.start() for m in re.finditer(w, code)]
        for o in occurences:
            word_occurences_queue.append([w, o])
    word_occurences_queue.sort(key=lambda a: a[1])
    
    for w in word_occurences_queue:
        w[0] = str(words_digits_list.index(w[0]))

    print(code)
    occurences = digits_occurences + word_occurences_queue
    occurences.sort(key=lambda a: a[1])
    values.append(int(occurences[0][0] + occurences[-1][0]))

print(values)
print("s = " + str(sum(values)))