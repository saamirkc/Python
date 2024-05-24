def translation(phrase):
    translation=''
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"g"
        else:
            translation=translation+letter
    return translation

print (translation(input("ENTER THE PHRASE : ")))