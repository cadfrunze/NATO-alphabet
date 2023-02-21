import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data_words = pandas.read_csv('nato_phonetic_alphabet.csv')




data_dict = {valoarea.letter: valoarea.code for (nimic, valoarea) in data_words.iterrows()}

print(data_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_answer = input('Zii ceva: ').capitalize()

user_answer = user_answer.replace(' ', '')
user_list = [letter for letter in user_answer]

print(user_list)

