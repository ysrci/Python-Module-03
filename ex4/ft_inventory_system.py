#!/usr/bin/python3.10

players = {
    "Alice":
        {
            "sword":
            {
                "type": "weapon",
                "rarity": "rare",
                "quantities": 1,
                "value": 500
            },
            "potion":
            {
                "type": "consumable",
                "rarity": "common",
                "quantities": 5,
                "value": 50
            },
            "shield":
            {
                "type": "armor",
                "rarity": "uncommon",
                "quantities": 1,
                "value": 200
            }
        },
    "Bob":
        {
            "magic_ring":
            {
                "type": "weapon",
                "rarity": "rare",
                "quantities": 1,
                "value": 700
            }
        }
}


if __name__ == "__main__":
    print("=== Player Inventory System ===")

    print("\n=== Alice's Inventory ===")
    all_total = 0
    count_item = 0
    wea = 0
    con = 0
    arm = 0
    for item, data in players.get("Alice").items():
        qty = data.get("quantities")
        value = data.get("value")
        type_ = data.get("type")
        rarity = data.get("rarity")

        total = qty * value
        all_total += total
        count_item += data.get("quantities")
        if type_ == "weapon":
            wea += qty
        elif type_ == "consumable":
            con += qty
        elif type_ == "armor":
            arm += qty

        print(
            f"{item} ({type_}, {rarity}): {qty}x @"
            f" {value} gold each = {total} gold"
        )

    print(f"\nInventory value: {all_total} gold")
    print(f"Item count: {count_item} items")
    print(f"Categories: weapon({wea}), consumable({con}), armor({arm})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    giver = players["Alice"]
    recever = players["Bob"]

    giver["potion"]["quantities"] -= 2
    recever.update({
        "potion": {
            "type": giver["potion"]["type"],
            "rarity": giver["potion"]["rarity"],
            "quantities": 2,
            "value": giver["potion"]["value"]
        }
    })
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {players['Alice']['potion']['quantities']}")
    print(f"Bob potions: {players['Bob']['potion']['quantities']}")

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: Alice ({all_total - (50 * 2)} gold)")
    print(f"Most items: Alice ({count_item - 2} items)")

    weapons = []
    for player, items in players.items():
        for item_name, data in items.items():
            if data.get("type") == "weapon":
                weapons.append(item_name)

    print("Rarest items:", ", ".join(weapons))
