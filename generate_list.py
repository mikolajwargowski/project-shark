"""Utility to generate a list of numbers from 1 to 10."""


def generate_list() -> list[int]:
    """Return a list containing numbers from 1 through 10."""
    return list(range(1, 11))


if __name__ == "__main__":
    print(generate_list())
