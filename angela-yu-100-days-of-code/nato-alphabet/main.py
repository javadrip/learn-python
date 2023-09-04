# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

phonetic_code_words = [ dictionary[letter] for letter in word]

print(phonetic_code_words)