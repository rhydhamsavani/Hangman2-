#Hangman

import random
wordBank = ["banana", "apple", "kiwi"]
chosenWord = random.choice(wordBank)
guessWord = []
userGuess = [] 

attempts = 3
for char in chosenWord:
    userGuess.append(char)
for char in chosenWord:
    guessWord.append((" _ "))


print(''.join(guessWord))

while(attempts != 0 and " _ " in guessWord): 
    userInput = input('Pick a letter from A-Z: ').lower()
    for x in range(len(chosenWord)):
        if userInput == userGuess[x]: 
            guessWord[x] = userInput
            
    if userInput not in chosenWord: 
        attempts = attempts - 1
        print('You Guessed Incorrectly.')
        print(f'You have {attempts} attempts remaining.')
        
    print(guessWord)

