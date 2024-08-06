import sys

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        count = 0
        for line in lines:
            line = line.strip()

            # Ignore blank lines
            if line == '':
                continue

            # Ignore comment lines
            if line.startswith('#'):
                continue

            count += 1

        return count

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Too few command-line arguments")
        sys.exit(1)

    # Check if the file has a valid extension
    filename = sys.argv[1]
    if not filename.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    # Count the lines of code
    num_lines = count_lines(filename)
    print(f"Number of lines of code: {num_lines}")
