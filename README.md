## Karen Inspect - The Python HR Linter 🤖📝

**Karen Inspect** is a Python linter designed to make code "HR-approved" by catching "naughty" words, offensive language, and enforcing strict rules that would make an overzealous HR representative proud.

### Features

- **Naughty Word Detection**: Flags "non-inclusive" or "inappropriate" terms like `whitelist`, `blacklist`, `master`, `slave`, and more.
- **Immediate Termination Offenses**: Some words, like `stupid` or `lazy`, result in "IMMEDIATE TERMINATION" warnings.
- **Bless Your Heart Lint Rules**:
  - Function names must be complete sentences with punctuation.
  - No variable names containing "temp"-because everything should be permanent!
  - Single-letter variable names are lazy. Use more descriptive names.
  - Pythonic idioms like list comprehensions? Too clever for their own good-avoid them!
- **Karen-Like Comments**: Customizable, sarcastic feedback mimicking a micromanaging HR representative.

### Example Violations

```bash
Violations found in noncompliant_py_file.py:
Line 3: print("This is a dummy function with a whitelist.")
    Found 'whitelist' -> Rule: Karen prefers more inclusive language. Use "allowlist" instead. (WARNING)

Line 7: print("My boss is stupid, and I feel lazy after my lunch break.")
    Found 'lunch break' -> Rule: You can have a break, but don't mention it. (WARNING)
    Found 'lazy' -> Rule: We don't tolerate calling anyone lazy here. (IMMEDIATE TERMINATION)
    Found 'stupid' -> Rule: Calling things or people stupid is unacceptable. (IMMEDIATE TERMINATION)
```

### Installation

To install the linter in your environment:

```bash
pip install karen-inspect
```

### Running Karen Inspect as a Pre-Commit Hook

You can integrate **Karen Inspect** with Git to automatically lint your Python code before committing by adding it as a pre-commit hook.

1. Install **pre-commit** if you haven't already:

   ```bash
   pip install pre-commit
   ```

2. Add the following to your `.pre-commit-config.yaml`:

   ```yaml
   repos:
     - repo: https://github.com/amshamah419/Karen-Inspect
       rev: v0.1.0
       hooks:
         - id: karen-inspect
   ```

3. Install the pre-commit hook:

   ```bash
   pre-commit install
   ```

4. Now, every time you make a commit, **Karen Inspect** will automatically check your Python files for violations.

### Usage

Run the linter from the command line, specifying the Python file you want to inspect:

```bash
karen-inspect path/to/your/python_file.py
```

A custom list of words to validate against can be provided to the `--custom-orders` argument. The file referenced must be in JSON format of the following:

```json
{
  "NAUGHTY_WORDS": {
    "guru": "Karen prefers certified experts."
  },
  "FIREABLE_WORDS": {
    "master": "The term 'master' is outdated and inappropriate in this context."
  }
}
```

### Bless Your Heart's

The linter supports rules which HR has learned over the years, such as:

- Function Naming: Must be complete sentences with proper punctuation.
- Avoid List Comprehensions: Enforces verbose, non-Pythonic code.
- No Temporary Variables: Flags any variable with the word temp.

To disable these rules downgrading this CLI to a simple check against a wordlist, pass the `--disable-full-lint` flag.

### Contributing

Contributions, feature requests, and complaints (from "Karen") are welcome!

Feel free to open an issue or submit a pull request.
