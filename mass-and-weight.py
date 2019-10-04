# Mass and Weight
# Shaun Hayworth
# CIS 2
# 10-03-2019

# Converts mass in kilograms to weight in newtons, and displays a message that the object is too heavy if it is over 500 newtons
# and too light if it is less than 100 newtons.

# Prompt user for mass in kilograms and stores the result in mass
mass = float(input('Please enter an object\'s mass in kg: '))

# Converts mass to weight in newtons by multiplying by 9.8
weight = mass * 9.8

# Display the result
print(f'\n{mass} kg is eqal to {weight} newtons.')

# If weight is above 500, prints a message saying the object is too heavy, and if weight is below 100, prints a message
# saying the object is too light.
if weight > 500:
  print('\nThis object is too heavy!')
elif weight < 100:
  print('\nThis object is too light!')
