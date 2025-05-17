def print_cyk_table(table, input_string):
    """
    Print the CYK table in a readable triangular format.
    Args:
        table (list): 2D list of sets representing the CYK table.
        input_string (list): Input string for labeling.
    """
    n = len(table)
    print("\nCYK Table:")
    # Print header with input string
    header = "    " + " ".join(f"{i}:{w:3}" for i, w in enumerate(input_string))
    print(header)
    print("    " + "-" * (n * 4))
    for i in range(n):
        row = f"{i}: "
        for j in range(n):
            if j < i:
                row += "    "  # Skip lower triangle
            else:
                cell = str(table[i][j]) if table[i][j] else "{}"
                row += f"{cell:3} "
        print(row)
    print()

def cyk_parse(grammar, input_string):
    """
    Parse a string using the CYK algorithm, showing the table at each step.
    Args:
        grammar (dict): CFG in CNF where keys are non-terminals and values are lists of productions.
        input_string (list): List of terminals to parse.
    Returns:
        bool: True if the string is accepted, False otherwise.
    """
    n = len(input_string)
    if n == 0:
        return False

    # Initialize the table as n x n with empty sets
    table = [[set() for _ in range(n)] for _ in range(n)]
    print("\nInitial Table:")
    print_cyk_table(table, input_string)

    # Fill the diagonal (length 1)
    for i in range(n):
        for non_terminal, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == input_string[i]:
                    table[i][i].add(non_terminal)
        print(f"After filling diagonal position {i} ({input_string[i]}):")
        print_cyk_table(table, input_string)

    # Fill the table for lengths 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for non_terminal, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            left, right = rule
                            if left in table[i][k] and right in table[k + 1][j]:
                                table[i][j].add(non_terminal)
            print(f"After processing substring from {i} to {j} (length {length}):")
            print_cyk_table(table, input_string)

    # Final result
    print("Final Table:")
    print_cyk_table(table, input_string)
    return 'S' in table[0][n - 1]

# Define the grammar
grammar = {
    'S': [['A', 'T']],
    'T': [['B', 'C']],
    'A': [['a']],
    'B': [['b']],
    'C': [['c']]
}

# Test the parser
input_strings = [
    ["a", "b", "c"],
    ["a", "b", "b"],
    ["a", "a", "a", "b", "c"]
]

for input_string in input_strings:
    print(f"\nTesting input: {' '.join(input_string)}")
    result = cyk_parse(grammar, input_string)
    print(f"Result: {'Accepted by grammar' if result else 'Not accepted by grammar'}\n")