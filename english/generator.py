# generator.py
"""
# Script to generate worksheet pdf
"""

from worksheets.simple_1 import generate_simple_1
from worksheets.abc_001 import generate_abc_001
from worksheets.abc_002 import generate_abc_002


def main():
    print("Generating worksheets...")

    # Generate the simple worksheet
    generate_simple_1()

    # Generate the ABC 4-line large practice worksheet
    generate_abc_001()

    # Generate the abc 4-line large practice worksheet
    generate_abc_002()

    print("All worksheets generated successfully.")



if __name__ == "__main__":
    main()
