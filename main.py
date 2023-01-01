import pandas
data_frames = pandas.read_csv("nato_phonetic_alphabet.csv")
symbols = {row.letter:row.code for(index, row) in data_frames.iterrows()}
user_name = input("What your name? ").upper()
symbol_name = [symbols[letter] for letter in user_name]
print(symbol_name)
