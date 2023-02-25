import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_words = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {valoarea.letter: valoarea.code for (nimic, valoarea) in data_words.iterrows()}

print(data_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def nato_alph(user_fun):
    user_fun = user_fun.replace(' ', '')
    user_list = [item for item in user_fun]
    new_dict = [data_dict[letter] for letter in user_list if letter in data_dict.keys()]
    return new_dict


while True:
    user_answer = input('Zii ceva: ').upper()
    if user_answer == 'EXIT':
        break
    print(nato_alph(user_fun=user_answer))
