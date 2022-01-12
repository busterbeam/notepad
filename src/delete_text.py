class delete_text:
    text = ""
    bad_words = ['bad', 'naughty']

    def delete_bad_words(word):
        with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in bad_words):
                    newfile.write(line)
        print()



bad_words = ['bad', 'naughty']


def delete_bad_words(word):
    with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)


delete_bad_words(bad_words)


def makeIndent(path: str, indentLength: int):
    f = open(path, 'r')
    data = f.read()
    lines = data.split("\n")
    new_data = ""
    for index in range(len(lines)):
        lines[index] = " " * indentLength + lines[index] + "\n"
        new_data += lines[index]

    f = open("new_code.txt", "w")
    f.write(new_data)


makeIndent("code.txt", 4)
