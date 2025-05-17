def cyk_parse(grammar, input_string):
    n = len(input_string)
    if n == 0:
        return False
    
    # Initialize the table as n x n with empty sets
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Fill the diagonal (length 1)
    for i in range(n):
        for non_terminal, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == input_string[i]:
                    table[i][i].add(non_terminal)
    
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
    
    # Return True if 'S' is in table[0][n-1]
    return 'S' in table[0][n - 1]

# Define the grammar
grammar = {
    'S': [['A', 'T']],
    'T': [['B', 'C']],
    'A': [['a']],
    'B': [['b']],
    'C': [['c']]
}

# S → A T
# (S generates an "a" followed by the rest, represented by T)
# T → B C
# (T generates "b" followed by "c")
# A → a
# (A generates the terminal "a")
# B → b
# (B generates the terminal "b")
# C → c
# (C generates the terminal "c")
# generates "a b c" as follows: S → A T → a T → a B C → a b C → a b c.

# Test the parser
input_string = ["a", "b", "c"]
result = cyk_parse(grammar, input_string)
print("Accepted by grammar" if result else "Not accepted by grammar")

# Additional test
input_string2 = ["a", "b", "b"]
result2 = cyk_parse(grammar, input_string2)
print("Accepted by grammar" if result2 else "Not accepted by grammar")

input_string3 = ["a", "a", "a", "b", "c"]
result3 = cyk_parse(grammar, input_string3)
print("Accepted by grammar" if result3 else "Not accepted by grammar")