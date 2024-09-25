import os
import sys
import click
from karen.orders import check_naughty_words, check_custom_lint_rules


class HRLinter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.violations = []

    def lint(self):
        """Lints the file for 'naughty' words and fire-able offenses."""
        try:
            with open(self.filepath, 'r') as f:
                lines = f.readlines()

            # Check for word-based violations
            for lineno, line in enumerate(lines, start=1):
                word_violations = check_naughty_words(line)
                if word_violations:
                    for word, rule, severity in word_violations:
                        self.violations.append((lineno, line.strip(), word, rule, severity))

            # Check for custom linting rules
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
@click.argument('filepath', type=click.Path(exists=True))
def main(filepath):
    """
    Lint the provided Python file for 'naughty' words and fire-able offenses.
    """
    if not os.path.isfile(filepath):
        click.echo(f"{filepath} is not a valid file.")
        sys.exit(1)

    linter = HRLinter(filepath)
    linter.lint()
    linter.report()


if __name__ == "__main__":
    main()
