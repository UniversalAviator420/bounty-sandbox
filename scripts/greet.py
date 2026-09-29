def greet(name):
    """Return a friendly greeting.

    Fix for issue #3 — `greet(None)` used to crash with AttributeError on
    `name.upper()`. Now falls back to "THERE" for None / empty / non-string
    inputs so callers don't have to pre-validate.
    """
    if not name or not isinstance(name, str) or not name.strip():
        return "Hello, THERE!"
    return "Hello, " + name.upper() + "!"


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print(greet(sys.argv[1]))
    else:
        # sanity self-checks covering the regression
        assert greet("makar") == "Hello, MAKAR!"
        assert greet(None) == "Hello, THERE!"
        assert greet("") == "Hello, THERE!"
        assert greet("   ") == "Hello, THERE!"
        print("greet self-check OK")
