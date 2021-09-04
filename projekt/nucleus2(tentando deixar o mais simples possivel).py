import random as r
answer, control = ".", False

def roll():
  dice = r.randint(1, 7)
  return dice

def make_1st_question():
  global answer, control
  answer, control = input("Do you wanna play? (Y/N) ").lower(), True
  verification()

def make_2nd_question():
  global answer, control 
  answer, control = input("Do you wanna play once more? (Y/N) ").lower(), False
  verification()

def verification():
  if answer == "yes" or answer == "y":
    print(f"This is your number: {roll()}"), make_2nd_question()
  elif answer == "no" or answer == "n":
    print("Baibai!")
  else:
    print("You made a typo! Type again slowly and calmly.")
    if control:
      make_1st_question()
    elif control == False:
      make_2nd_question()

make_1st_question()
