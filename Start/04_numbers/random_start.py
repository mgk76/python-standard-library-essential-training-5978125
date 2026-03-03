# demonstrate using the random module to create random numbers
import random

# TODO: create a random number
print(random.random())
print()

# TODO: implement a coin toss function
print("Heads" if random.random() <= 0.5 else "Tails")
print()

# TODO: get a random number within a range
# incl 1, excl 100
print(random.uniform(1, 100))

# TODO: generate random integers within a given range
print(random.randint(1, 100))

# TODO: generate random integers with a step function
# this example chooses from 0 to 100 stepped by 5
print(random.randrange(0, 100, 5))

# TODO: Use the seed function to position the generator
print()
print("Use Seed")
random.seed(1)
print(random.random())
print(random.random())
print("----------------")
random.seed(1)
print(random.random())
print(random.random())