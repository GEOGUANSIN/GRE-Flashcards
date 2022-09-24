import pandas as pd
from random import randint
import webbrowser as wb
import os


# Check repetition
def is_repetition(current_i, memo_i):
    repeat = False
    if current_i in memo_i:
        repeat = True
    return repeat


# Prevent repetition
def choosing(n, memo_, random_=True):
    if random_:
        choice_ = randint(0, n - 1)
        if n > 4:
            # noinspection PyUnboundLocalVariable
            while is_repetition(choice_, memo_):
                choice_ = randint(0, n - 1)
            del memo_[0]
            memo_.append(choice_)
        return choice_, memo_
    else:
        if memo_[0] == n - 1:
            choice_ = 'end'
            return choice_, memo_
        else:
            memo_[0] = memo_[0] + 1
            choice_ = memo_[0]
            return choice_, memo_


# Change directory
cwd = os.getcwd()
cwd += '\Flashcard Stacks'
print(f'You are now at {cwd}')
os.chdir(cwd)

# Initiate the desired stack
while True:
    end = False
    c = input(
        'Which Stack? '
        '\n (0) GRE Top 52 '
        '\n (1) GRE 1 '
        '\n (2) GRE Kaplan '
        '\n (3) GRE 2 (1-100) '
        '\n (4) GRE 2 (100-260) '
        '\n (e) Exit'
    )
    if c in ['0', '1', '2', '3', '4', 'e']:
        if c == '0':
            df = pd.read_csv('GRETop52.csv')
        elif c == '1':
            df = pd.read_csv('GRE1.csv')
        elif c == '2':
            df = pd.read_csv('GRE Kaplan.csv')
        elif c == '3':
            df = pd.read_csv('GRE2-1-100.csv')
        elif c == '4':
            df = pd.read_csv('GRE2-100-260.csv')
        elif c == 'e':
            end = True
            break
        # noinspection PyUnboundLocalVariable
        n = len(df.index)
        if n > 4:
            memo = [0, 1, 2, 3, 4]  # for later check
        print('')
        break
    else:
        print('There is no such option. Try again.')

# Initiate the mode
while True and end != True:
    mode = input('Which mode? '
                 '\n (1) Random '
                 '\n (2) Index '
                 '\n (e) Exit'
                 '\n'
                 )
    if mode == '1':
        is_random = True
        break
    elif mode == '2':
        is_random = False
        memo = [-1]
        break
    elif mode == 'e':
        end = True
        break
    else:
        print('There is no such option. Try again.')

# Looping through the stack randomly
while True and end != True:
    # noinspection PyUnboundLocalVariable
    choice, memo = choosing(n, memo, is_random)
    if choice == 'end':
        print('You have reach the end of the list.')
        break
        # noinspection PyUnboundLocalVariable
    word = df.iloc[choice]['Word']
    print('Word:\n', word)
    x = input('Meaning:')
    if x == 'exit':  # check for exit
        break
    print('', df.iloc[choice]['Meaning'], '\n')
    y = input('Next? \n (Or type 1 to exit, 2 to search)')  # give choices
    if y == 'exit' or y == '1':
        break
    if y == '2':
        wb.open_new('https://www.google.com/search?q=meaning+of+' + word)
    print('\n')

input('Type anything to exit.')
