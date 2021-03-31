import random, time

def main():
    randNum = vytvorCislo()
    #print(type(randNum) , randNum) # aux. for debuging
    underLine = '-'*47
    printGreeting(underLine)

    iterNo = 0
    Tstart = time.time()
    while True:
        print(underLine)
        playerInp = input('Your choice: ')
        if playerInp == 'q':
            print('Program stop on user input')
            break
        elif inputCheck(playerInp):
            continue
        else:
            iterNo += 1
            bullNo, cowNo = numberEval(randNum, playerInp)
            if len(bullNo) == 4:
                Tend = time.time()
                print(f'''Correct, you've guessed the right number
in {iterNo} guesses!
{underLine}
You needed: {Tend - Tstart: 10.2f} seconds''')
                break
    print('End of game!')


def numberEval(randNumb: str, playerNumb: str) -> str:
    bulls = [item for i, item in enumerate(playerNumb) if item == randNumb[i]]
    rest = list(set(randNumb).difference(bulls))
    cows = [itm for itm in rest if playerNumb.count(itm)]
    print(f'{len(bulls)} bull{"s" if len(bulls) != 1 else ""}, {len(cows)} cow{"s" if len(cows) != 1 else ""}')
    return bulls, cows

def inputCheck(playInp: str) -> bool:
    if len(playInp) != 4:
        print('Number must have 4 digits')
        return True
    elif not playInp.isdecimal():
        print('Your input is not a number')
        return True
    elif playInp[0] == '0':
        print('0 as fist number is not allowed')
        return True
    elif len(set(playInp)) != 4:
        print('Duplicated characters in your number are not allowed')
        return True
    else:
        return False

def vytvorCislo() ->int:
    numLst = list(range(1, 10))
    random.shuffle(numLst)
    rand_num = ''.join(map(str, numLst[0:4]))
    return rand_num

def printGreeting(underline: str) ->None:
    print(f'''Hi there!
{underline}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{underline}
Enter a number (for quit enter "q"):''')

main()