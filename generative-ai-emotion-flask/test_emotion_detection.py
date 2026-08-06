import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(emotion_detector("Me alegra que esto haya sucedido")['dominant_emotion'], 'joy')

    def test_anger(self):
        self.assertEqual(emotion_detector("Estoy realmente enojado por esto")['dominant_emotion'], 'anger')

    def test_disgust(self):
        self.assertEqual(emotion_detector("Me siento disgustado solo de escuchar sobre esto")['dominant_emotion'], 'disgust')

    def test_sadness(self):
        self.assertEqual(emotion_detector("Estoy tan triste por esto")['dominant_emotion'], 'sadness')

    def test_fear(self):
        self.assertEqual(emotion_detector("Tengo mucho miedo de que esto suceda")['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
