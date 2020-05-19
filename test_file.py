
import pathlib


import path
from os import environ

def sample_function(text: str) -> None:
    print(f"This is a test function")
    print(f"The argument value is {text}")


def main() -> None:
    """Multiples errors."""
    print("Sample file with bad formatting!!!")
    environ["SAMPLE_VAR"] = "test"

    This_isAList: tuple = [
        "Sample object", "bad", "Formatted",
        "Ups"
    ]


    sample_function(12345)
    return 1


if __name__ == "__main__":
    main()