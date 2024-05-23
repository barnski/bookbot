def count_letters():
    letters = {}

    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()

        for l in file_contents.lower():
            if l.isalpha():
                if l in letters:
                    letters[l] += 1
                else:
                    letters[l] = 1

    return letters


def main():
    letters = count_letters()

    
    l = []
    for letter, count in letters.items():
        l.append({"count": count, "letter": letter})

    l.sort(key=lambda x: x["count"], reverse=True)

    for letter in l:
        # The 'e' character was found 46043 times
        print(f'The \'{letter["letter"]}\' character was found {letter["count"]} times')

main()
