# Mass and Weight
# Shaun Hayworth
# CIS 2
# 10-03-2019

# Converts mass in kilograms to weight in newtons, and displays a message that the object is too heavy if it is over 500 newtons
# and too light if it is less than 100 newtons.

# This version of the program uses functions for converting mass to weight, and to loop the program indefinitely until the user
# tells it to stop.

# This function converts mass to weight using the formula weight = mass * 9.8 
def convert_to_weight(mass):
    return mass * 9.8
  
# Asks user if they would like to run the program again, and sets the run_again varible to false if not.
def repeat_query():
  repeat = ''
  while repeat != 'y' or repeat != 'Y' or repeat != 'n' or repeat != 'N':
    repeat = input('Would you like to run the program again (y/n)? ')
    if repeat == 'y' or repeat == 'Y':
        return True
    elif repeat == 'n' or repeat == 'N':
      return False
  
# main program function
def main():
  # Prompt user for mass in kilograms and stores the result in mass
  mass = float(input('Please enter an object\'s mass in kg: '))
  
  # Call function to convert mass to weight
  weight = convert_to_weight(mass)
  
  # Display the result
  print(f'\n{mass} kg is eqal to {weight} newtons.')

  # If weight is above 500, prints a message saying the object is too heavy, and if weight is below 100, prints a message
  # saying the object is too light.
  if weight > 500:
    print('\nThis object is too heavy!')
  elif weight < 100:
    print('\nThis object is too light!')
    
# Set the run_again variable to True by default
run_again = True

# Loops the main program as long as run_again is True
while run_again == True:
  print("\033c") # Clears the screen
  main()
  another_time = repeat_query()
  run_again = another_time
