from translator import french_to_english, english_to_french

import unittest

class TestFrenchLanguageTranslation(unittest.TestCase):

    def setUp(self):
        self.f2e = french_to_english("Bonjour")

    def test_french_to_english_response(self):
        self.assertEqual(type(self.f2e), str)

    def test_french_to_english_text(self):
        self.assertIsNotNone(self.f2e)


class TestEnglishLanguageTranslation(unittest.TestCase):

     def setUp(self):
         self.e2f = english_to_french("Hello")

     def test_english_to_french_response(self):
         self.assertEqual(type(self.e2f), str)

     def test_english_to_french_text(self):
         self.assertIsNotNone(self.e2f)



if __name__ == '__main__':
    unittest.main()
