import os
import sys
import json
import click

from karen.orders import check_naughty_words, check_custom_lint_rules, get_default_orders


class HRLinter:
    def __init__(self, orders, filepath):
        self.orders = orders
        self.filepath = filepath
        self.violations = []

    def lint(self, disable_lint_rules=False):
        """Lints the file for 'naughty' words and fire-able offenses."""
        try:
            with open(self.filepath, 'r', encoding="utf-8") as f:
                lines = f.readlines()

            # Check for word-based violations
            for lineno, line in enumerate(lines, start=1):
                word_violations = check_naughty_words(self.orders, line)
                if word_violations:
                    for word, rule, severity in word_violations:
                        self.violations.append((lineno, line.strip(), word, rule, severity))


            # Check for custom linting rules
            if not disable_lint_rules:
                custom_violations = check_custom_lint_rules(self.filepath)
                for lineno, line, word, rule, severity in custom_violations:
                    self.violations.append((lineno, line, word, rule, severity))

        except FileNotFoundError:
            print(f"File {self.filepath} not found.")
            sys.exit(1)

    def report(self):
        """Prints the violations in a human-readable format."""
        if not self.violations:
            print(f"No violations found in {self.filepath}.")
        else:
            print(f"Violations found in {self.filepath}:")
            for lineno, line, word, rule, severity in self.violations:
                print(f"Line {lineno}: {line}")
                if severity == "termination":
                    print(f"    Found '{word}' -> Rule: {rule} (IMMEDIATE TERMINATION)\n")
                elif severity == "bless-heart":
                    print(f"    Found '{word}' -> Rule: {rule} (I've been around the block a few times okay?)\n")
                else:
                    print(f"    Found '{word}' -> Rule: {rule} (MANDATORY SENSITIVITY TRAINING REQUIRED)\n")


@click.command()
@click.argument('filepaths', type=click.Path(exists=True), nargs=-1)
@click.option('--custom-orders', type=click.Path(exists=True), help='Path to a file containing the custom list of orders')
@click.option('--disable-full-lint', is_flag=True, help='Disables HR lint rules, leaving only wordlist checks')
def main(filepaths, custom_orders, disable_full_lint):
    """
    Lint the provided Python file for 'naughty' words and fire-able offenses.
    """
    orders = get_default_orders()
    if custom_orders:
        with open(custom_orders, 'r') as f:
            orders = json.load(f)
    for filepath in filepaths:
        if not os.path.isfile(filepath):
            click.echo(f"{filepath} is not a valid file.")
            sys.exit(1)
        linter = HRLinter(orders, filepath)
        linter.lint(disable_full_lint)
        linter.report()



if __name__ == "__main__":
    main()
