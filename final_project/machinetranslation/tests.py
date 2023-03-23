"""Unity test"""
import unittest
from translator import english_to_french, french_to_english


class EnglishToFrenchTest(unittest.TestCase):
    """Class translate English to French"""
    def test(self):
        """First test"""
        self.assertEqual(english_to_french(
            ''), ('Bad request!', 500), "First case null response")
        self.assertEqual(english_to_french('Hello'),
                         'Bonjour', "Expectect response Bonjour")


class FrenchToEnglishTest(unittest.TestCase):
    """Class translate French to English"""
    def test(self):
        """Secund test"""
        self.assertEqual(french_to_english(
            ''), ('Bad request!', 500), "First case null response")
        self.assertEqual(french_to_english('Bonjour'),
                         'Hello', "Expectect response Hello")


if __name__ == '__main__':
    unittest.main()
