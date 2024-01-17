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


# Example 1: Merlin
# Path :clearbit_connector.py
# Example 2: Merlin
# merlin/merlin/scripts/Init perimeters from data.ipynb
# Example 3: Loth
# loth/defense/api/analysis_results/recommendation_comment/views.py
# Example 4: Loth
# loth/defense/api/comparison_board/views.py
# Example 5: perceval
# perceval/fair/utils/risk_prediction/claim_simulation.py
