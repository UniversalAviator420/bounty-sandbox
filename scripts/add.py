def add(a, b):
    """Return the sum of a and b.

    Regression fix for issue #5 — this used to subtract instead of add.
    """
    return a + b


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        a, b = float(sys.argv[1]), float(sys.argv[2])
        print(add(a, b))
    else:
        # quick sanity self-check
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        print("add self-check OK")
