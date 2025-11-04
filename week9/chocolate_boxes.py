# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maya Ayoubi
#               Divya Challa        
#               Gia Huynh
#               Kingston Alexander
# Section:      509
# Assignment:   Team Lab 10
# Date:         02 Nov 2025
#################################################################################

import random

def make_boxes(chocolates, max_attempts=3000):
    """
    Creates 25 boxes with 4 truffles each following the given rules:
    - No two truffles in a box are identical ([type, shape, filling, topping])
    - No box has both caramel and vanilla creme
    - No box has both nuts and sprinkles
    - No box has both square and rectangle shapes
    - Boxes that contain dark chocolate must contain 2–3 dark truffles
    Uses all truffles exactly once.
    Returns: list of lists, each with 4 truffle IDs
    """
    truffle_ids = list(chocolates.keys())
    n_truffles = len(truffle_ids)
    n_boxes = n_truffles // 4

    def is_valid(box, tid):
        """Check if tid can be added to box without breaking any rule."""
        cocoa, shape, filling, topping = chocolates[tid]
        combos = [chocolates[i] for i in box]
        fillings = [chocolates[i][2] for i in box]
        toppings = [chocolates[i][3] for i in box]
        shapes = [chocolates[i][1] for i in box]
        dark_count = sum(1 for i in box if chocolates[i][0] == "dark")

        # No identical truffles
        if [cocoa, shape, filling, topping] in combos:
            return False

        # Forbidden filling pairs
        if ("caramel" in fillings and filling == "vanilla") or ("vanilla" in fillings and filling == "caramel"):
            return False

        # Forbidden topping pairs
        if ("nuts" in toppings and topping == "sprinkles") or ("sprinkles" in toppings and topping == "nuts"):
            return False

        # Forbidden shape pairs
        if ("square" in shapes and shape == "rectangle") or ("rectangle" in shapes and shape == "square"):
            return False

        # Dark chocolate rule
        if cocoa == "dark":
            dark_count += 1
        if dark_count > 3:
            return False
        if len(box) == 3:  # if this would be the last truffle
            if dark_count > 0 and not (2 <= dark_count <= 3):
                return False

        return True

    for attempt in range(max_attempts):
        random.shuffle(truffle_ids)
        boxes = [[] for _ in range(n_boxes)]
        remaining = truffle_ids[:]
        success = True

        for tid in truffle_ids:
            placed = False
            random_order = list(range(n_boxes))
            random.shuffle(random_order)
            for j in random_order:
                if len(boxes[j]) < 4 and is_valid(boxes[j], tid):
                    boxes[j].append(tid)
                    placed = True
                    break
            if not placed:
                success = False
                break

        # Check if all boxes are full
        if success and all(len(b) == 4 for b in boxes):
            # Final check: dark-chocolate rule across all boxes
            all_valid = True
            for box in boxes:
                darks = sum(1 for i in box if chocolates[i][0] == "dark")
                if darks != 0 and not (2 <= darks <= 3):
                    all_valid = False
                    break
            if all_valid:
                return boxes  # ✅ success!

    raise RuntimeError("Failed to create valid boxes after many attempts. Try increasing max_attempts.")

# Example test
if __name__ == "__main__":
    chocolates = {1: ["milk", "round", "toffee", "sprinkles"],
2: ["milk", "square", "coconut", "none"],
3: ["dark", "heart", "strawberry", "white chocolate drizzle"],
4: ["dark", "round", "toffee", "white chocolate drizzle"],
5: ["milk", "square", "caramel", "nuts"],
6: ["milk", "heart", "toffee", "dark chocolate drizzle"],
7: ["dark", "rectangle", "caramel", "none"],
8: ["dark", "heart", "strawberry", "white chocolate drizzle"],
9: ["dark", "heart", "coconut", "white chocolate drizzle"],
10: ["milk", "square", "coconut", "none"],
11: ["milk", "round", "vanilla", "dark chocolate drizzle"],
12: ["milk", "round", "strawberry", "nuts"],
13: ["milk", "rectangle", "caramel", "sprinkles"],
14: ["dark", "rectangle", "toffee", "none"],
15: ["dark", "heart", "toffee", "none"],
16: ["dark", "heart", "coconut", "white chocolate drizzle"],
17: ["dark", "round", "vanilla", "none"],
18: ["dark", "rectangle", "toffee", "dark chocolate drizzle"],
19: ["milk", "round", "toffee", "none"],
20: ["milk", "square", "caramel", "dark chocolate drizzle"],
21: ["milk", "square", "vanilla", "none"],
22: ["dark", "heart", "caramel", "sprinkles"],
23: ["milk", "square", "caramel", "nuts"],
24: ["milk", "round", "caramel", "dark chocolate drizzle"],
25: ["milk", "round", "coconut", "dark chocolate drizzle"],
26: ["dark", "round", "coconut", "dark chocolate drizzle"],
27: ["milk", "rectangle", "strawberry", "sprinkles"],
28: ["white", "heart", "vanilla", "none"],
29: ["dark", "heart", "strawberry", "none"],
30: ["dark", "rectangle", "caramel", "none"],
31: ["white", "round", "caramel", "none"],
32: ["milk", "heart", "vanilla", "none"],
33: ["white", "round", "strawberry", "nuts"],
34: ["milk", "round", "coconut", "none"],
35: ["dark", "rectangle", "coconut", "dark chocolate drizzle"],
36: ["milk", "round", "vanilla", "dark chocolate drizzle"],
37: ["dark", "round", "coconut", "white chocolate drizzle"],
38: ["dark", "round", "coconut", "white chocolate drizzle"],
39: ["dark", "round", "coconut", "dark chocolate drizzle"],
40: ["dark", "round", "strawberry", "dark chocolate drizzle"],
41: ["milk", "rectangle", "toffee", "none"],
42: ["milk", "round", "strawberry", "white chocolate drizzle"],
43: ["milk", "heart", "coconut", "none"],
44: ["white", "round", "strawberry", "white chocolate drizzle"],
45: ["milk", "heart", "toffee", "sprinkles"],
46: ["milk", "rectangle", "strawberry", "none"],
47: ["white", "round", "caramel", "dark chocolate drizzle"],
48: ["white", "square", "toffee", "none"],
49: ["milk", "rectangle", "toffee", "none"],
50: ["dark", "rectangle", "caramel", "none"],
51: ["milk", "square", "vanilla", "none"],
52: ["dark", "round", "toffee", "dark chocolate drizzle"],
53: ["milk", "round", "toffee", "white chocolate drizzle"],
54: ["dark", "square", "strawberry", "none"],
55: ["milk", "heart", "caramel", "dark chocolate drizzle"],
56: ["milk", "heart", "vanilla", "none"],
57: ["milk", "heart", "caramel", "none"],
58: ["milk", "heart", "coconut", "sprinkles"],
59: ["milk", "heart", "vanilla", "sprinkles"],
60: ["dark", "square", "caramel", "none"],
61: ["milk", "rectangle", "vanilla", "none"],
62: ["milk", "heart", "toffee", "none"],
63: ["milk", "heart", "vanilla", "dark chocolate drizzle"],
64: ["white", "round", "coconut", "white chocolate drizzle"],
65: ["milk", "round", "coconut", "nuts"],
66: ["milk", "round", "coconut", "white chocolate drizzle"],
67: ["dark", "heart", "coconut", "none"],
68: ["dark", "square", "toffee", "none"],
69: ["dark", "round", "strawberry", "dark chocolate drizzle"],
70: ["milk", "heart", "caramel", "none"],
71: ["milk", "square", "caramel", "sprinkles"],
72: ["milk", "rectangle", "strawberry", "sprinkles"],
73: ["dark", "heart", "strawberry", "none"],
74: ["dark", "heart", "strawberry", "none"],
75: ["dark", "square", "coconut", "none"],
76: ["dark", "heart", "caramel", "none"],
77: ["dark", "heart", "coconut", "nuts"],
78: ["white", "rectangle", "caramel", "dark chocolate drizzle"],
79: ["milk", "heart", "vanilla", "sprinkles"],
80: ["white", "heart", "strawberry", "none"],
81: ["dark", "round", "toffee", "white chocolate drizzle"],
82: ["dark", "round", "vanilla", "none"],
83: ["white", "square", "coconut", "none"],
84: ["milk", "rectangle", "caramel", "dark chocolate drizzle"],
85: ["white", "heart", "toffee", "none"],
86: ["white", "round", "caramel", "nuts"],
87: ["white", "round", "caramel", "none"],
88: ["dark", "round", "caramel", "none"],
89: ["dark", "square", "coconut", "nuts"],
90: ["milk", "heart", "vanilla", "none"],
91: ["dark", "round", "coconut", "none"],
92: ["dark", "round", "caramel", "none"],
93: ["white", "round", "toffee", "none"],
94: ["milk", "round", "vanilla", "sprinkles"],
95: ["white", "round", "strawberry", "white chocolate drizzle"],
96: ["dark", "square", "strawberry", "nuts"],
97: ["milk", "round", "vanilla", "none"],
98: ["milk", "rectangle", "caramel", "sprinkles"],
99: ["milk", "heart", "vanilla", "none"],
100: ["dark", "rectangle", "strawberry", "white chocolate drizzle"],
}


    boxes = make_boxes(chocolates)
    print("Boxes created:")
    for i, box in enumerate(boxes, 1):
        print(f"Box {i}: {box}")
    print("Total boxes:", len(boxes))
    print("Total truffles used:", sum(len(b) for b in boxes))