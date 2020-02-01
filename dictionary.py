import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif (len(get_close_matches(word, data.keys())) > 0):
        response = input('Did you mean %s instead? Enter y for yes, or n for no: ' % get_close_matches(word, data.keys())[0])
        if (response == 'y' or response.lower() == 'y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif (response == 'n' or response.lower() == 'n'):
            return 'The word doesn\'t exist. Please double check the input.'
        else:
            return 'Invalid input. Please try again.'
    else:
        return 'The word doesn\'t exist. Please double check the input.'

while True:
    word = input('Enter a word: ')

    output = translate(word)

    if (isinstance(output, list)):
        for index, item in enumerate(output):
            print('%s.) %s' % ((index + 1), item))
    else:
        print(output)

    loopResponse = input('\nWould you like to enter another word: Enter y for yes, or n for no: ')
    if (loopResponse == 'y' or loopResponse.lower() == 'y'):
        continue
    elif (loopResponse == 'n' or loopResponse.lower() == 'n'):
        print('terminating...')
        break
    else:
        print('Invalid input. \nterminating...')
        break