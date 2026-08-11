import unittest
from EmotionDetection.utils import map_label_to_emotion
from EmotionDetection.preprocess import clean_text

class EmotionDetectionTest(unittest.TestCase):
    def test_map_label(self):
        self.assertEqual(map_label_to_emotion(2), "joy")
        self.assertEqual(map_label_to_emotion(5), "surprise")
        self.assertEqual(map_label_to_emotion(99), "unknown")

class PreprocessTest(unittest.TestCase):
    def test_clean_text_basic(self):
        text = "Hello!!! This is a TEST."
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello this is a test")

    def test_clean_text_links(self):
        text = "Check this http://example.com now!"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "check this now")

    def test_clean_text_symbols(self):
        text = "I #love$ AI!!!"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "i love ai")


if __name__ == "__main__":
    unittest.main()
