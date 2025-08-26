from math_utils import *

def run_tests():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5.0
    try:
        divide(5, 0)
    except ValueError:
        print("Divide-by-zero test passed.")
    else:
        raise AssertionError("Expected ValueError")

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()