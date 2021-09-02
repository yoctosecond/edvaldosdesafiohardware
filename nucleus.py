#@title Dice Number Generator for Edvaldos

import random as r
import time as t

answer = "waiting for yes or no"           # generic sentence
sorted_number = False                      # generic value

def ignition():                            # this starts the program
  global answer
  answer = create_question(0)

  if answer == "yes" or answer == "y":     # if the user insert a "yes" argument
    roll_the_dice()
  elif answer == "no" or answer == "n":    # if the user insert a "no" argument
    t.sleep(2)
    print("Bₐᵢ bₐᵢ :₍")
    return
  else:                                    # if the user inserts a invalid argument
    t.sleep(2)

    print("Please enter a valid argument, silly kid!")
    ignition()

def roll_the_dice():                       # part 2 (gives us a random number from one to six)
  global sorted_number

  t.sleep(1)
  print("Generating your random number... ")
  t.sleep(2)
  create_empty_lines()

  sorted_number = r.randrange(1, 7)        # the core of the program (random number)
  print_the_score()

def print_the_score():                     # part 3 (displays the number to the user)
  global answer

  create_stars()
  print(f"٭ 𝗧𝗵𝗶𝘀 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗰𝗵𝗼𝘀𝗲𝗻 𝗻𝘂𝗺𝗯𝗲𝗿: {sorted_number}")
  send_a_nice_message()
  create_stars()
  create_empty_lines()

  answer = '...'                           # it sets again the value of "answer" for a generic response

  t.sleep(2)
  reconfirmation()

def reconfirmation():                      # part 4 (confirm again that the user wants to play)
  global answer

  answer = create_question(1)
  if answer == "yes" or answer == "y":     # if the user insert a "yes" argument
    recapitulation()
  elif answer == "no" or answer == "n":    # if the user insert a "no" argument
    print("Bₐᵢ bₐᵢ :₍")
    return
  else:                                    # if the user inserts a invalid argument
    t.sleep(2)
    print("Please enter a valid argument, silly kid!")
    reconfirmation()

def recapitulation():                      # final (repeat the code if the answer is yes or y)
  create_empty_lines()
  print("───────✧❁✧───────" * 15)
  create_empty_lines()
  roll_the_dice()

def create_empty_lines():                  # just create empty lines for stylish purposes
  print("\n")

def create_question(choose):               # just a system that changes between inputs
  if choose == 0:
    return input("Do you wanna play some dice? (𝙚𝙣𝙩𝙚𝙧 with [𝙮𝙚𝙨] or [𝙮] / [𝙣𝙤] or [𝙣] to 𝙘𝙖𝙣𝙘𝙚𝙡) ")
  elif choose == 1:
    return input("Do you wanna play again? (𝙚𝙣𝙩𝙚𝙧 with [𝙮𝙚𝙨] or [𝙮] / [𝙣𝙤] or [𝙣] to 𝙘𝙖𝙣𝙘𝙚𝙡) ")

def create_stars():                        # a function that prints STARSSS *-*
  print("٭" * 28)

def send_a_nice_message():                 # generate a cool message
  if sorted_number == 1:
    print("٭ Oh! Nice try! Do not give up :D")
  elif sorted_number == 2:
    print("٭ Haha! Maam, this man got a two!")
  elif sorted_number == 3:
    print('٭ Plant more "threes" to save our WORLD! *-*')
  elif sorted_number == 4:
    print('٭ You have got a four! This is "four" you baby :)')
  elif sorted_number == 5:
    print("٭ A 5, dang this! Almost there, DON'T GIVE UP!!! >:(")
  elif sorted_number == 6:
    print("٭ MUHAHAHAHAHAHA! YOU DID IT! YOU DID A SUCCESSFUL ATTACK! >:D")

ignition()
