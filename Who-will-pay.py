# in an Restaurant when the bill arrives and a random card is to be selcted 
#we will use random module 

import random
# Initialize an empty list to store names
People= []

# Define the number of names you want to input
num_People= int(input("Enter the number of names: "))

# Use a loop to get each name from the user
for _ in range(num_People):
    name = input("Enter a name: ")
    People.append(name)

print("name list = ",People)
#picking a random person using random.choice function.
print("Person who has to pay ->",random.choice(People))

