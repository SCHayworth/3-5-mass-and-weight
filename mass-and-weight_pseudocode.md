## Scope
Scientists measure an object's mass in kilograms and its weight in newtons. If you know the amount of mass of an object in
kilograms, you can calculate its weight in newtons with the following formula:

    weight = mass x 9.8

Write a program that asks the user to enter an object's mass, then calculates its weight. If the object weighs more than 500
newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons, display a message
indicating that it is too light.

## Pseudocode
    Prompt user for the mass of an object in kg and store input in a variable.
    calculate the object's weight in newtons
      mass * 9.8 = weight
    IF weight > 500
      display "This object is too heavy!"
    ELSE IF weight < 100
      display "This object is too light!"
      
## Alternate Pseudocode
    Define a function to convert mass in kg to weight in newtons
      convert(mass)
        mass * 9.8
    Prompt user for the mass of an object in kg
    Call convert function using input as a parameter and store the result in a weight variable.
    IF weight > 500 
      display "This object is too heavy!"
    ELSE IF weight < 100
      display "This object is too light!"
