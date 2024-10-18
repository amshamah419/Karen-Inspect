import ast
import re
import json


def get_default_orders() -> list:
    orders = []
    with open('karen/assets/orders.json', 'r') as f:
        orders = json.load(f)
    return orders


def check_naughty_words(orders, line):
    """Check if the line contains any naughty words or fire-able offenses."""
    violations = []
    # Check for naughty words (full word match only)
    for word, rule in orders.get('NAUGHTY_WORDS', {}).items():
        # Use regular expression to match whole words only
        if re.search(rf'\b{re.escape(word)}\b', line):
            violations.append((word, rule, "warning"))

    # Check for fire-able words (full word match only)
    for word, rule in orders.get('FIREABLE_WORDS', {}).items():
        # Use regular expression to match whole words only
        if re.search(rf'\b{re.escape(word)}\b', line):
            violations.append((word, rule, "termination"))

    return violations


def check_custom_lint_rules(filepath):
    violations = []

    with open(filepath, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    tree = ast.parse("".join(lines), filename=filepath)

    # 2. Check for function names that are not complete sentences
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            if not (re.search(r'\s', func_name) and func_name.endswith('.')):
                violations.append((
                    node.lineno,
                    lines[node.lineno - 1].strip(),  # Add the offending line content
                    "Grammar Nazi",                        # Indicate this is a custom rule
                    'Function names should be complete sentences with proper punctuation.',
                    'bless-heart'
                ))

    # 3. Check for variables with the word 'temp'
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if 'temp' in node.id.lower():
                violations.append((
                    node.lineno,
                    lines[node.lineno - 1].strip(),
                    "Hi-Tech Karen",
                    "No temporary variables allowed. Everything should have a permanent purpose.",
                    'bless-heart'
                ))

    # 5. Check for single-letter variable names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and len(node.id) == 1:
            violations.append((
                node.lineno,
                lines[node.lineno - 1].strip(),
                "Grammar Nazi",
                'Single-letter variables are lazy. Use descriptive names.',
                'bless-heart'
            ))

    # 7. Check for list comprehensions (avoid Pythonic idioms)
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            violations.append((
                node.lineno,
                lines[node.lineno - 1].strip(),
                "Hi-Tech Karen",
                'Avoid Pythonic shortcuts like list comprehensions. They are too clever for their own good.',
                'bless-heart'
            ))

    return violations
