#!/usr/bin/python3.10
import math


def distance_3d(p1, p2):
    """ Distance 3D"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (math.sqrt((x2 - x1)**2 +
                      (y2 - y1)**2 +
                      (z2 - z1)**2))


def parse_coordinates(coort_str):
    """Parse Coordinates"""
    parts = coort_str.split(",")
    try:
        return (int(parts[0]),
                int(parts[1]),
                int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)
        return None


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    pos_1 = (10, 20, 5)

    print(f"\nPosition created: {pos_1}")
    print(f"Distance between {origin} and {pos_1}: "
          f"{distance_3d(origin, pos_1):.2f}")

    pos_2 = "3,4,0"
    print('\nParsing coordinates: "3,4,0"')
    pos = parse_coordinates(pos_2)
    if (pos):
        print(f"Parsed position: {pos}")
        print(f"Distance between {origin} and {pos}: "
              f"{distance_3d(origin, pos):.1f}")

    pos_3 = "abc,def,ghi"
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parse_coordinates(pos_3)

    print("\nUnpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
