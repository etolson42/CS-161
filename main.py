# Student: Eric Tolson
# Lab3_PartA: Questions 1 and 2
# This program converts a read temp from Celsius to Fahrenheit and simulates a two-dice roll based on side-value input.


import random


def tempConvert(t):
    """This function converts a Celsius temperature to a Fahrenheit temperature."""
    conversion = (t * (9/5)) + 32
    return conversion


def diceRoll(d1, d2):
    """This function creates the sum a two dice roll."""
    roll = d1 + d2
    return roll


def main():
    temperature = float(input("Please enter a degree value for a Celsius temperature: "))
    print(str(temperature) + " degrees Celsius is " + str(tempConvert(temperature)) + " degrees Fahrenheit.")
    maxroll = int(input("How many sides do your dice have? "))
    dice1 = random.randint(1, maxroll)
    dice2 = random.randint(1, maxroll)
    print("Your roll is " + str(diceRoll(dice1, dice2)) + ".")


if __name__ == "__main__":
    main()
