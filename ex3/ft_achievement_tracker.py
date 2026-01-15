#!/usr/bin/python3.10

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = set(['first_kill',
                 'level_10',
                 'treasure_hunter',
                 'speed_demon'])
    bob = set(['first_kill',
               'level_10',
               'boss_slayer',
               'collector'])
    charlie = set(['level_10',
                   'treasure_hunter',
                   'boss_slayer',
                   'speed_demon',
                   'perfectionist'])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    union_ = alice.union(bob).union(charlie)
    print(f"All unique achievements: {union_}")
    print(f"Total unique achievements: {len(union_)}")

    inter_ = alice.intersection(bob).intersection(charlie)
    print(f"\nCommon to all players: {inter_}")

    diff_ = union_.difference(
        alice.intersection(bob)
        .union(alice.intersection(charlie))
        .union(bob.intersection(charlie)))
    print(f"Rare achievements (1 player): {diff_}")

    defr_ = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {defr_}")

    uni_ = alice.difference(bob)
    print(f"Alice unique: {uni_}")

    dif_ = bob.difference(alice)
    print(f"Bob unique: {dif_}")
