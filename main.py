import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)  # For debugging purposes only. Print df to console.
print(data.to_dict())

# Create a phonetic dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)  # For debugging purposes only. Print phonetic dictionary

# Create a list of the phonetic code words from a word that the user inputs
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)  # For debugging purposes only.




