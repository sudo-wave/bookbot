def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    num_words = count_words(file_contents)
    chars_dict = get_chars(file_contents)
    chars_lst = count_chars(chars_dict)
    report = get_report(path, num_words, chars_lst)
    print(report)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    text = text.split()
    return len(text)


def get_chars(text):
    text = text.lower()
    chars_dict = {}
    for char in text:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict


def count_chars(d):
    lst = []
    for k in d:
        if k.isalpha():
            tmp = {"letter": k, "num": d.get(k)}
            lst.append(tmp)
    return lst


def get_report(path, num_words, char_lst):
    char_lst.sort(reverse=True, key=sort_on)
    report = (
        "--- Begin report of "
        + path
        + " ---\n"
        + str(num_words)
        + " words found in the document\n\n"
    )
    for c in char_lst:
        s = "The letter '" + c["letter"] + "' was found " + str(c["num"]) + " times\n"
        report = report + s
    report = report + "--- End report ---"
    return report


def sort_on(d):
    return d["num"]


main()
