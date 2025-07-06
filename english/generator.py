# generator.py
"""
# Script to generate worksheet pdf
"""

from worksheets.simple_1 import generate_simple_1
from worksheets.abc_001 import generate_abc_001


def main():
    print("Generating worksheets...")

    # Generate the simple worksheet
    generate_simple_1()

    # Generate the ABC 4-line large practice worksheet
    generate_abc_001()

    print("All worksheets generated successfully.")



if __name__ == "__main__":
    main()
