# Student: Eric Tolson
# Lab3_PartA: Questions 1 and 2
# This program converts a read temp from Celsius to Fahrenheit and simulates a two-dice roll based on side-value input.


import random


def tempConvert(t):
    """This function converts a Celsius temperature to a Fahrenheit temperature."""
    return (t * (9/5)) + 32


def diceRoll(s):
    """This function creates the sum a two dice roll."""
    return random.randint(1, s) + random.randint(1, s)


def main():
    temperature = float(input("Please enter a degree value for a Celsius temperature: "))
    print(str(temperature) + " degrees Celsius is " + str(tempConvert(temperature)) + " degrees Fahrenheit.")
    maxroll = int(input("How many sides do your dice have? "))
    print("Your roll is " + str(diceRoll(maxroll)) + ".")


if __name__ == "__main__":
    main()
