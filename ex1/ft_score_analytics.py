#!/usr/bin/python3.10
import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    my_list = sys.argv
    i = 1
    x = 1

    list_int = []
    try:
        while i < len(my_list):
            list_int.append(int(my_list[i]))
            i += 1
    except ValueError:
        print(f"oops, I typed '{my_list[i]}' instead of '1000'")
        x = 0

    if len(list_int) == 0:
        print("No scores provided. Usage: python3",
              "ft_score_analytics.py <score1> <score2> ...")
        x = 0

    if x == 1:
        print(f"Scores processed: {list_int}")
        print(f"Total players: {len(list_int)}")
        print(f"Total score: {sum(list_int)}")
        print(f"Average score: {sum(list_int) / len(list_int)}")
        print(f"High score: {max(list_int)}")
        print(f"Low score: {min(list_int)}")
        print(f"Score range: {max(list_int) - min(list_int)}")
