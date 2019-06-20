import random
import winsound
import time

class bcolors:
    HEADER = '\033[95m'
    RED2 = '\33[91m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKGREEN_2 = '\033[43m'
    GREEN = '\33[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\33[3m'
    VIOLET2 = '\33[35m'

quotes = []
insults = []

users = {
    'i': 0,
    'd': 0
}
user_names = {
    'i': "Ian>>>",
    'd': "Donat>>>"
}

game_stats = {
    'rounds': 0,
    'i':0,
    'd':0
}
rating = {
        1: 'Genius!',
        2: 'Prodigy!',
        3: 'Amateur...',
        4: 'Idiot :(',
        5: 'Dipshit ;('
}

def beep():
    for x in range(200):
        freq = 500
        duration = 200
        period = random.uniform(0.01, 0.1)
        character = random.randint(40, 120)
        time.sleep(period)
        winsound.Beep(freq, duration)
        print(chr(character))

def load_quotations():
    file_one = open('quotes.txt', 'r')
    file_two = open('insults.txt', 'r')
    for line in file_one:
        quotes.append(line)
    for line in file_two:
        insults.append(line)

def decorated_print(string):
    print("*" * len(string))
    print(bcolors.WARNING + string.strip('\n') + bcolors.ENDC)
    print("*" * len(string))

def print_quote():
    number = random.randint(0, len(quotes)-1)
    decorated_print(quotes[number])

def insult_user():
    number = random.randint(0, len(insults) - 1)
    decorated_print(insults[number])

def accept(attempts):
    try:
        print("Damn right! It took you {2}{0}{3} guesses! You are a {1}".format(attempts, rating[attempts], bcolors.OKGREEN, bcolors.ENDC))
        if attempts <= 3: print_quote()
        if attempts >= 4: insult_user()
    except KeyError:
        print("Damn right! It took you {} guesses! Try again, and again...?".format(attempts))
        insult_user()
    guess()

def evaluate(user_input):

    global user
    global answer

    if user_input == '666':
        users['i'] = users['d'] = 0
        guess()
    elif user_input == 666:
        users['i'] = users['d'] = 0
        guess()
    else:
        if isinstance(user_input, str):
            user = user_input.lower()
        elif isinstance(user_input, int):
            answer = user_input
        else:
            pass

def intoduction():
    print("\n****Welcome to the Wild Wild Guess!****")
    print("\tScores \t Rounds: {5}\n{2}Ian:{4} \t{3}{0}{4}\n{2}Donat:{4} \t{3}{1}{4}\n".format(users['i'], users['d'], bcolors.VIOLET2,
                                                                                bcolors.OKBLUE, bcolors.ENDC, int(game_stats['rounds'])
                                                                                               ))
#def results():
#    print("\tTotal rounds played: {0}\n\tSuccess Rate\n{1}:\t{2}\n{3}:\t{4}\n".format(game_stats['rounds'], users['i'], (game_stats['rounds']/2.0)/(game_stats['i'])*100.0, users['d'], (game_stats['rounds']/2.0)/(game_stats['d'])*100.0))


def guess():

    #START
    attempts = 0
    number = random.randint(0, 10)

    intoduction()
    evaluate(input('Who are you?'))

    while game_stats['rounds'] <= 4:

        try:
            user_input = int(input(bcolors.VIOLET2 + user_names[user] + bcolors.ENDC))
            evaluate(user_input)
        except ValueError:
            attempts += 1
            game_stats[user]+=1
            print("Wrong input!")
            continue
        except KeyError:
            print("Wrong user! Try again.")
            guess()
        if answer > number:
            attempts+=1
            game_stats[user] += 1.0
            print(bcolors.RED2 + "Too high!" + bcolors.ENDC)
            continue
        elif answer < number:
            attempts+=1
            game_stats[user] += 1.0
            print(bcolors.OKBLUE +  "Too low!" + bcolors.ENDC)
            continue
        else:
            attempts+=1
            game_stats[user] += 1.0
            users[user]+=(11-attempts)
            game_stats['rounds']+=0.5
            accept(attempts)

        #results()

load_quotations()
guess()









