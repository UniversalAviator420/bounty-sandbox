def greet(name=None):
    """Greets a person by name, or defaults to 'THERE' if name is None or empty."""
    if not name:
        return "Hello, THERE!"
    return "Hello, " + name.upper() + "!"
