def anti_alphabetical_letters(thing):
    letters = []
    for letter in thing:
        if isinstance(letter,str):
            letters +=letter
        else:
            if isinstance(letter, list):
                letters += anti_alphabetical_letters(letter)
    return ''.join(sorted(set(letters),reverse=True))

print (anti_alphabetical_letters([['abc','a','cbaaa','u'],['aga']]))
