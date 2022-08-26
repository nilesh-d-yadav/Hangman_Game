

from replit import clear
from ascii_art import stages,logo
import random
from list_of_words import word_list

print(logo)
chosen_word=random.choice(word_list).lower()
display=[]

for letter in chosen_word:
  display+="_"
print(display)

all_filled=False
lives=6

while(not all_filled):
  guess=input("\nGuess the letter: ").lower()
  clear()
  
  if guess in display:
      print(f"You have already guessed {guess}\n")
    
  for a in range(0,len(chosen_word)):
    if guess==chosen_word[a]:
      display[a]=guess
      
  
  
  if guess not in chosen_word:
    print(f"'{guess}' is not in the word. You lose a life\n")
    lives-=1
    print(f"\nYou have {lives}/6 remaining lives")
    if lives==0:
      all_filled=True
      print("\nYou lose")
      
  print(stages[lives-1])
      
  print("\n")
  print(display) 

  if "_" not in display:
    print(f"\n\nYou WIN\nYou guessed '{chosen_word}' with {lives} lives remaining ")
    all_filled=True
