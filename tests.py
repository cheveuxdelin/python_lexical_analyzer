import unittest
from lexical_analyzer import LexicalAnalyzer

transitions_path = "transitions.csv"


class TestLexicalAnalyzer(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_empty_prompt(self):
        self.assertEqual(LexicalAnalyzer(transitions_path).analyze(""), [])

    def test_code_1(self):
        test_code_path = "test_files/file1.c"
        self.assertEqual(LexicalAnalyzer(transitions_path).analyze_from_file(test_code_path), [])

    def test_code_2(self):
        test_code_path = "test_files/file2.c"
        self.assertEqual(LexicalAnalyzer(transitions_path).analyze_from_file(test_code_path), [])

    def test_code_3(self):
        test_code_path = "test_files/file3.c"
        self.assertEqual(LexicalAnalyzer(transitions_path).analyze_from_file(test_code_path), [])
