def pig_latin(text):
    say = ""
    center_word = ""
    # Separate the text into words
    words = text.split(" ")
    for word in words:
        # Create the pig latin word and add it to the list
        word = list(word)
        first_letter = word.pop(0)
        for letter in word:
            center_word += letter
        say = say + " " + center_word + first_letter + "ay"
        center_word = ""
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
