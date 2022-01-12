def leave_specified_text(good_words):
    with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
        for line in oldfile:
            if any(good_word in line for good_word in good_words):
                newfile.write(line)


def return_list_by_each_line(path):
    file = open(path)
    text = file.read()
    lines = text.split("\n")
    return lines


lines = return_list_by_each_line("good.txt")
leave_specified_text(lines)
