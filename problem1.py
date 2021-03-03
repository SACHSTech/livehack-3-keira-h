"""
----------------------------------------------------------
Name:    problem1.py
Purpose: Write a program to determine which group a player is placed in

Author:  Hosey.K

Created: date in 03/03/2021
----------------------------------------------------------
"""

# Header of tracker
print("~~~~~~~~~~~~ Tournament Tracker ~~~~~~~~~~~~")

# Input wins and losses
win_count = 0

for i in range(6):
  game = input("Enter the wins and losses for your team: ")
  if game == "W":
    win_count += 1

# Determining Group
if win_count >= 5:
  print("Your team is in Group 1.")
elif (win_count == 3) or (win_count == 4):
  print("Your team is in Group 2.")
elif (win_count == 1) or (win_count == 2):
  print("Your team is in Group 3.")
else:
  print("Your team is eliminated from the tournament.")
