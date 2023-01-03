#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 2, 2023
# This program prints the integers from 1000 to 2000,
# outputting five integers per line with each
# separated by a space.
import math


def main():
    for counter in range(1000, 2001):
        # Outputs integers with a space between each
        print(counter, end=" ")
        # If the current integer is divisible by 5, go to the next line
        if counter % 5 == 4:
            print("")


if __name__ == "__main__":
    main()
