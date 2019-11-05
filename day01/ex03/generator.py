import random


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if not isinstance(text, str):
        return 'ERROR'
    if option and option not in ['shuffle', 'unique', 'ordered']:
        return 'ERROR'
    if option == 'shuffle':
        textlist = text.split(sep=sep)
        random.shuffle(textlist)
        for elem in textlist:
            yield elem
        pass
    elif option == 'unique':
        textlist = text.split(sep=sep)
        myset = set(textlist)
        textlist = list(myset)
        for elem in textlist:
            yield elem
    elif option == 'ordered':
        textlist = (text.split(sep=sep))
        textlist = sorted(textlist, key=str.lower)
        for elem in textlist:
            yield elem
    elif option is None:
        textlist = text.split(sep=sep)
        for elem in textlist:
            yield elem


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)
