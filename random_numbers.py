# TODO import the library to randomly generate numbers
import random


def generator(n, starting, ending):
    """
    This function generates multiple random integer numbers, and return them as
    a list.

    @param n (int), number of numbers to generate
    @param starting (int), starting value of the random number range, inclusive
    @param ending (int), ending value of the random number range, inclusive

    @return (list), put all generated random integers into a list, and return it
    """

    numbers = []

    # TODO: use loop to generate n random integers between starting and ending, then append the random number into the list
    for _ in range(n):
        rand_num = random.randint(starting, ending)
        numbers.append(rand_num)

    return numbers


if __name__ == "__main__":
    print(generator(5, 1, 10))   # 5 numbers between 1 and 10
    print(generator(3, -5, 5))   # 3 numbers between -5 and 5
