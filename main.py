# Student: Eric Tolson
# Lab5_PartB

def summer(loopAmount):
    """This function loops an integer prompt as many times as the argument value and returns the sum of those inputs."""
    totalSum = 0
    for num in range(loopAmount):
        num = int(input("Enter a number: "))
        totalSum += num
    print("The sum is " + str(totalSum))
    return totalSum


def average(sumInput, divideAmount):
    """This function divides a sum by an amount and returns an average."""
    print("The average is " + str(sumInput / divideAmount))
    return sumInput / divideAmount


def main():
    # set loopAmount argument to integer input
    loopAmount = int(input("How many numbers do you want to add? "))

    # set sumInput argument to summer function return
    sumInput = summer(loopAmount)

    # call average function with summer function return and loopAmount
    average(sumInput, loopAmount)


if __name__ == "__main__":
    main()
