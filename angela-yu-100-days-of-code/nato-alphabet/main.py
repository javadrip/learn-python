# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(dictionary)


def generate_phonetic():
    # 2. Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()

    try:
        phonetic_code_words = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(phonetic_code_words)


generate_phonetic()
