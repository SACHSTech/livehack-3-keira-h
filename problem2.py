"""
----------------------------------------------------------
Name:    problem2.py
Purpose: Write a program that allows Tony to enter the distance driven for each day until the total distance driven surpasses 100km

Author:  Hosey.K

Created: date in 03/03/2021
----------------------------------------------------------
"""

# Header of tracker
print("~~~~~~~~~ Welcome to the DoorDash Distance Tracker ~~~~~~~~~")
print("")

# Travel log title
print("~~~~~~ Travel Log ~~~~~~")

# Input distance travelled
number_days = 0
distance_per_day = 0 
total_distance = 0

while distance_per_day < 100:
  distance_per_day = float(input("Enter the distance travelled for the day: "))
  number_days += 1
  total_distance += distance_per_day
  if total_distance > 100:
    break

# Summary title
print("")
print("~~~~~~~ Summary ~~~~~~~")

# Output Message
print("It took",number_days,"days to surpass 100 km driven.")

average = total_distance//number_days
print("The average distance driven per day is",average,"km.")
