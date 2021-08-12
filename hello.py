"""
This is a test.
"""

def add(x_0, y_0):
    """
    Adding Function
    """
    return x_0 + y_0


RESULT = add(1, 2)
print(f"1, 2, {RESULT}")
def mul(x_0, y_0):
    """Multiplication Function"""
    return x_0 * y_0


NEW = mul(4, 5)

print(f"Multiplication 4 x 5 = {NEW}")

def sub(x_0, y_0):
    """Subtraction Function"""
    return x_0 - y_0

X_1 = 20
Y_1 = 4
NEW_RESULT = sub(X_1, Y_1)
print(f"subtraction {X_1} - {Y_1} = {NEW_RESULT}")
