# Structural Pattern Matching 3.10
point = (2, 3)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-Axis at x={x}")
    case (0, y):
        print(f"Y-Axis at y={y}")
    case (x, y):
        print(f"Point at x={x}, y={y}")
    case _:
        print("Not a point")
