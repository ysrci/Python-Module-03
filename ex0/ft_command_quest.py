#!/usr/bin/python3.10
import sys

if __name__ == "__main__":
    my_list = sys.argv
    print("=== Command Quest ===")

    if len(my_list) == 1:
        print("No arguments provided!")

    print(f"Program name: {my_list[0]}")

    if len(my_list) > 1:
        print(f"Arguments received: {len(my_list) - 1}")
        x = 1
        while x < len(my_list):
            print(f"Argument {x}: {my_list[x]}")
            x += 1

    print(f"Total arguments: {len(my_list)}")
