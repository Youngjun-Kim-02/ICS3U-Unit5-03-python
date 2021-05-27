#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions


def calculate_mark(level):

    if level == "1-":
        percentage = "51"
    elif level == "1":
        percentage = "55"
    elif level == "1+":
        percentage = "58"
    elif level == "2-":
        percentage = "61"
    elif level == "2":
        percentage = "65"
    elif level == "2+":
        percentage = "68"
    elif level == "3-":
        percentage = "71"
    elif level == "3":
        percentage = "75"
    elif level == "3+":
        percentage = "78"
    elif level == "4-":
        percentage = "83"
    elif level == "4":
        percentage = "90"
    elif level == "4+":
        percentage = "97"
    else:
        return -1

    return percentage


def main():
    
    level = input("Enter the level you want converted to a percentage: ")
    
    # call functions
    calculated_mark = calculate_mark(level)
    
    if calculated_mark == -1:
        print("It is not a mark.")
    else:
        print("level {0} has a middle percentage"
            " of {1}%.".format(level, calculated_mark))


if __name__ == "__main__":
    main()
