from art import logo , vs
from game_data import data
import random

def pick():
  result = random.choice(data)
  return result

def a_or_an(name):
  if name[0] in ["A","E","I","O","U"]:
    return "an"
  else:
    return "a"
    
def versus_on_screen(a,b,score = 0):
  name_A = a["name"]
  description_A = a["description"]
  city_A = a["country"]
  follower_A = a["follower_count"]
  
  name_B = b["name"]
  description_B = b["description"]
  city_B = b["country"]
  follower_B = b["follower_count"]

  print(logo)
  if score > 0:
      print(f"You're right! Current score: {score}.")
  print(f"Compare A: {name_A}, {a_or_an(description_A)} {description_A}, from {city_A}")
  print(vs)
  print(f"Against B: {name_B}, {a_or_an(description_B)} {description_B}, from {city_B}")

  
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  if not ((follower_A > follower_B and answer == "a") or (follower_A < follower_B and answer == "b")):
    print(f"Sorry, that's wrong. Final score: {score}")
    return

  versus_on_screen(b,new_pick(b), score + 1)  
  
def versus():
  compare_A = pick()
  against_B = pick()
  while compare_A == against_B:
    against_B = pick()
  versus_on_screen(compare_A,against_B)
  
def new_pick(b):
  res = pick()
  while b == res:
     res = pick()
  return res  

versus()