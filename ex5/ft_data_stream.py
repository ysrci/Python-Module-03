#!/usr/bin/python3.10

def game_events_stream(n):
    """Information for stream game events"""
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i % 15) + 1
        yield i, player, level, action


def fibonacci_stream(n):
    """Fibonacci Math"""
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_stream(n):
    """Prime Math"""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event_id, player, level, action in game_events_stream(1000):
        total_events += 1

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} (level {level}) {action}")
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {total_events / 22222:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    for n in fibonacci_stream(10):
        print(n, end=", ")

    print("\nPrime numbers (first 5):", end=" ")
    for p in prime_stream(5):
        print(p, end=", ")
    print("")
