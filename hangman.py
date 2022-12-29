def printHangMan(theGuess,theWrongs) :
    line="-"*len(theGuess)
    print(theGuess)
    print(line)
    print(theWrongs)

def replaceCharAtIndex(theText,theChar,theIndex):
    return theText[:theIndex] + theChar + theText[theIndex+1:]

import random
wordList = ["football", "cherry", "calendar", "pattern", "abstract", "shocking", "musicality", "notepad", "abhor", "dashing", "christmas", "basketball", "stationary", "exotic",]
x = random.randint(1, 14)
print("Guess the Word")
Word = wordList[x]
count=len(Word)

# prepare
MyGuess=" "*count
MyWrong=""

printHangMan(MyGuess,MyWrong)

while len(MyWrong) < count and MyGuess!=Word:
    guess=input("make a guess: ")
    if len(guess)>1 :
        guess = guess[0]

    index=-1
    found=False
    while True :
        index = Word.find(guess,index + 1)
        if index==-1 :
            break

        found=True
        MyGuess = replaceCharAtIndex(MyGuess,guess,index)

    if not found:
        MyWrong = MyWrong + guess
       
    printHangMan(MyGuess,MyWrong)
if len(MyWrong) == count:
    print("Game Over! Word was", Word)
if MyGuess==Word:
    print("You did it!")