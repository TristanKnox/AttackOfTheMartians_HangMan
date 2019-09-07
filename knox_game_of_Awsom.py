import time
import random
from Combined_Animation import phase_in_hero2
from Combined_Animation import import_unit
from Combined_Animation import monster_animation
from Validation import choice_validation 
from Animation import ship_line_animation
from Animation import space_ship_in
#hero = import_unit(open("Hero.txt"))
phase_in_hero = []
#phrase = []
#blank = []
#word_1 =open("list_1.txt")
#word_2 = open("list_2.txt")
#word_3 = open("list_3.txt")
#word_4 = open("list_4.txt")
#word_5 = open("list_5.txt") 
word_1 = []
word_2 = []
word_3 = []
word_4 = []
word_5 = []
bad_guess = 0
#b_letters_guessed = []
#letters_guessed = []

#def menue():
    
def game():
    monster_count = 0
    #loops untill win seting are met
    while win_or_not_win() != True:
        print()
        print("It is your job to guess the sommoning phrase and sommon a Hero of Old \nTo save the world!!!\n")
        print("But dont take too lone or the Martian will phase in befor you sommon the Hero.")
        print("\n\n\n")
        #print("\nHint:(\nQuantity)(Adjective)(Noun)(Adjective)(Verb)")        
       # print(" ".join(phrase))
        #print("\n")
        print(" ".join(blank))

        print("\n")
        print("Letters Guessed:")
        for word in letters_guessed:
            print(word,",", end="")
        print()
       

#prints bad Guesses
        if len(b_letters_guessed) > 0 or len(b_word_guess) > 0:
            print("Incorrect Guesses:")
            if len(b_letters_guessed) > 0:
                #print("\n")
                #print("Incorrect Guesses:")
                for word in b_letters_guessed:
                    print(word,",", end="")
                #print(",")
            if len(b_word_guess) > 0:
                print()
                for word in b_word_guess:
                    print(word,end=",")
                    #print("\n")
        print("\n\n\n")
        guess = input("Guess a letter:\nOR\nIf you think you can complete a word.\nGuess a word:\n")
        
#check for bad guess 
    #play monster phase in if bad
        if len(guess) > 1:
            if word_guess(guess) == False:
                monster_animation()
                monster_count +=1
                print(monster_count)
        else:
            if letter_guess(guess) == False:
                monster_animation()
                monster_count +=1
                print(monster_count)
        if monster_count == 7:
            for count in range(1,10):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("          You have lost!!!!")
                print("\n\n\n\n\n\n\n\n")
                time.sleep(.5)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                for line in import_unit(open("monster.txt")):
                    print(line)
                time.sleep(.5)
            return "loss"
            
            
            
    
    
    #win_or_not_win()    
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
def populat_word_lists():
    #populat word_1
    for line in open("list_1.txt"):
        line = line.strip()
        word_1.append(line)
    #pepulat word_2
    for line in open("list_2.txt"):
        line = line.strip()
        word_2.append(line)
    #populat word_3
    for line in open("list_3.txt"):
        line = line.strip()
        word_3.append(line)
    #populat word_4
    for line in open("list_4.txt"):
        line = line.strip()
        word_4.append(line)
    #populat word_5
    for line in open("list_5.txt"):
        line = line.strip()
        word_5.append(line)

#uses word lists to generate phrase        
def phrase_gernerator():
    word = random.choice(word_1)
    for cycle in range(1,6):
        if cycle == 1:
            phrase.append(random.choice(word_1))
            #phrase.append(" ")
        elif cycle == 2:
            phrase.append(random.choice(word_2))
            #phrase.append(" ")
        elif cycle == 3:
            phrase.append(random.choice(word_3))
            #phrase.append(" ")
        elif cycle == 4:
            phrase.append(random.choice(word_4))
            #phrase.append(" ")
        else:
            phrase.append(random.choice(word_5))
            #phrase.append(" ")
    #phrase_str = ""
    #for word in phrase:
    #    phrase_str += word
    #print(phrase_str)
    #return phrase_str

#uses phrase to generate the blank phrase	
def generate_blank_list():
    for index in range(0,len(phrase)):
        str = ""
        if len(phrase[index]) != 1:
            for cycle in range(0,len(phrase[index])):
                str += "."
            blank.append(str)
#checks to see if guess is in phrase
def letter_guess(guess):
    b = 0
    for p_index in range(0,len(phrase)):
        blank_word = blank[p_index]
        for word_index in range(0,len(phrase[p_index])):
            if guess == phrase[p_index][word_index]:
                blank_word = blank_word[:word_index] + guess + blank_word[word_index+1:]
            elif guess.upper() == phrase[p_index][word_index]:
                blank_word = blank_word[:word_index] + guess.upper() + blank_word[word_index+1:]
                blank_word.capitalize()
        if blank_word.find(guess) == -1 and blank_word.find(guess.upper()) == -1:
            b += 1
        if len(phrase[p_index]) > 1:
            blank.remove(blank[p_index])
            blank.insert(p_index ,blank_word)
        if b == 5:
            b_letters_guessed.append(guess)
            return False
    letters_guessed.append(guess)

            

def win_or_not_win():
    counter = -1
    for index in range(0,len(phrase)):
        
        if phrase[index] == blank[index]:
            counter += 1
        if counter == len(phrase)-1:
            return True

    return False

def word_guess(guess):
    b_counter = 0
    for index in range(0,len(phrase)):
        print(index)
        if guess.capitalize() == phrase[index]:
            guess = guess.capitalize()
            blank.remove(blank[index])
            blank.insert(index,guess)
            return True
        else:
            b_counter += 1
        if b_counter == len(phrase):
            b_word_guess.append(guess)
            return False
             
            


populat_word_lists()
space_ship_in()
ship_line_animation() 
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Will You?")
menue_choice = input("1: To play game\n2: To exit\n")
choice = choice_validation(menue_choice,"menu")
while choice == 1:
    phrase = []
    blank = []
    b_letters_guessed = []
    letters_guessed = []
    b_word_guess = []
    phrase_gernerator()
    generate_blank_list()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if game() != "loss":
        phase_in_hero2(import_unit(open("Hero.txt")),phase_in_hero)
        for count in range(1,10):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("          You have won!!!!")
            print("\n\n\n\n\n\n\n\n")
            time.sleep(.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            for line in import_unit(open("Hero.txt")):
                print(line)
            time.sleep(.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    space_ship_in()
    ship_line_animation() 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Will You?")
    menue_choice = input("1: To play again\n2: To exit\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")    
print("I figured you didnt have it in you anyway!\nGood by.")
    #pycharm
    

    