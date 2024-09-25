# tests/test_linter.py

import unittest
from karen.inspection import HRLinter


class TestPythonLinter(unittest.TestCase):

    def test_no_violations(self):
        linter = HRLinter("tests/test_files/compliant_py_file.py")
        linter.lint()
        self.assertEqual(len(linter.violations), 0)

    def test_violations(self):
        linter = HRLinter("tests/test_files/noncompliant_py_file.py")
        linter.lint()
        self.assertGreater(len(linter.violations), 0)


if __name__ == '__main__':
    unittest.main()
