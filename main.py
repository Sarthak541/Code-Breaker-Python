import random
GUESSES = {"G","R","B"}   #Set of all possible guesses
GUESS_VALUES = {0:"G",1:"R",2:"B"} #Dictionary used to create random guesses

#Function to print the rules of the game to the terminal
def rules()->None:
    print("Guess the pattern to break the code! Guesses should be G(for green) \
           \nR(for Red) or B(for Blue). Guesses should be seperated by commas.  \
          \n3 colors should be guessed. Example G,R,B")
    
#Function to read the input line and return a list of guesses, guesses should be G(for green)
#R(for Red) or B(for Blue).  Guesses should be seperated by commas.  3 colors should be guessed
def parse_line()->list:
    to_parse = input().split(",")
    if len(to_parse)!=3:
        print("Make sure to guess only 3 colors")
        to_parse = parse_line() #Recursion runs parse_line until the right value is inputed
    for i in to_parse:
        if (i not in GUESSES) and (i.upper() not in GUESSES):
            print(f"The first invalid input is {i}")
            to_parse = parse_line() 
            break
    return to_parse

#Function to generate guesses
def generate_guess()->list:
    guess = []
    for i in range(3):
        guess.append(GUESS_VALUES[random.randint(0,2)])
    return guess
        



def play():
    rules()
    to_guess = generate_guess()
    #print(to_guess) if you want to cheat
    hit = 0
    num_guesses = 0
    while num_guesses<5:
        guess = parse_line()
        for i in range(len(guess)):
            if guess[i].upper() == to_guess[i]:
                hit+=1
        if hit == 3:
            break
        print(f"You hit {hit}!")
        num_guesses+=1
        hit = 0
    if hit == 3:
        print("you won!")
    else:
        print("you lost!")
    


play()