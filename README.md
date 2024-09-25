## Karen Inspect - The Python HR Linter 🤖📝

**Karen Inspect** is a Python linter designed to make code "HR-approved" by catching "naughty" words, offensive language, and enforcing strict rules that would make an overzealous HR representative proud.

### Features

- **Naughty Word Detection**: Flags "non-inclusive" or "inappropriate" terms like `whitelist`, `blacklist`, `master`, `slave`, and more.
- **Immediate Termination Offenses**: Some words, like `stupid` or `lazy`, result in "IMMEDIATE TERMINATION" warnings.
- **Bless Your Heart Lint Rules**:
  - Function names must be complete sentences with punctuation.
  - No variable names containing "temp"—because everything should be permanent!
  - Single-letter variable names are lazy. Use more descriptive names.
  - Pythonic idioms like list comprehensions? Too clever for their own good—avoid them!
- **Karen-Like Comments**: Customizable, sarcastic feedback mimicking a micromanaging HR representative.

### Example Violations

```bash
Violations found in noncompliant_py_file.py:
Line 3: print("This is a dummy function with a whitelist.")
    Found 'whitelist' -> Rule: Karen prefers more inclusive language. Use "allowlist" instead. (WARNING)

Line 7: print("My boss is stupid, and I feel lazy after my lunch break.")
    Found 'lunch break' -> Rule: You can have a break, but don’t mention it. (WARNING)
    Found 'lazy' -> Rule: We don’t tolerate calling anyone lazy here. (IMMEDIATE TERMINATION)
    Found 'stupid' -> Rule: Calling things or people stupid is unacceptable. (IMMEDIATE TERMINATION)
```

### Installation
To install the linter in your environment:

```bash
git clone https://github.com/amshamah419/Karen-Inspect
cd karen-inspect
pip install .
```

### Usage
Run the linter from the command line, specifying the Python file you want to inspect:

```bash
karen-inspect path/to/your/python_file.py
```

### Bless Your Heart's
The linter supports rules which HR has learned over the years, such as:

- Function Naming: Must be complete sentences with proper punctuation.
- Avoid List Comprehensions: Enforces verbose, non-Pythonic code.
- No Temporary Variables: Flags any variable with the word temp.

### Contributing
Contributions, feature requests, and complaints (from "Karen") are welcome!

Feel free to open an issue or submit a pull request.