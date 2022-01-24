def do():
    original_text = input("\nwrite text to reverse by word : ").lower()
    reversed_text = ""
    splited_or_txt = original_text.split()
    reversed_text = list(map(lambda txt: txt[::-1], splited_or_txt))
    reversed_text = " ".join(reversed_text)
    print("\n{}".format(reversed_text))
    do()

do()
