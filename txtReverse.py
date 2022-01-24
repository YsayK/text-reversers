def do():
    global original_text
    global reversed_text

    original_text = input("\nнеповторимый оригинал : ")
    reversed_text = ""

    i = len(original_text) - 1

    while(i >= 0):
        reversed_text = reversed_text + original_text[i]
        i -= 1

    print("жалкое пародие : {}".format(reversed_text))
    do()


do()
