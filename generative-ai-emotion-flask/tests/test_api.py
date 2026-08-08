import unittest
from unittest.mock import patch
import json
from app import create_app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    # ---------------------------
    # GET SUCCESS
    # ---------------------------
    @patch("EmotionDetection.bert_emotion_model.EmotionModel.predict")
    def test_predict_get_success(self, mock_predict):
        mock_predict.return_value = (2, [[0.1, 0.1, 0.7, 0.05, 0.03, 0.02]])  # joy

        resp = self.client.get("/emotionDetector", query_string={"textToAnalyze": "I love this"})
        self.assertEqual(resp.status_code, 200)

        data = resp.get_json()
        self.assertEqual(data["emotion"], "joy")
        self.assertIn("probabilities", data)

    # ---------------------------
    # GET INVALID
    # ---------------------------
    def test_predict_get_invalid(self):
        resp = self.client.get("/emotionDetector", query_string={"textToAnalyze": ""})
        self.assertEqual(resp.status_code, 400)

        data = resp.get_json()
        self.assertIn("error", data)

    # ---------------------------
    # POST SUCCESS
    # ---------------------------
    @patch("EmotionDetection.bert_emotion_model.EmotionModel.predict")
    def test_predict_post_success(self, mock_predict):
        mock_predict.return_value = (3, [[0.05, 0.05, 0.10, 0.70, 0.05, 0.05]])  # love

        payload = {"textToAnalyze": "I really love this!"}
        resp = self.client.post(
            "/emotionDetector",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["emotion"], "love")
        self.assertIn("probabilities", data)

    # ---------------------------
    # JSON STRUCTURE
    # ---------------------------
    @patch("EmotionDetection.bert_emotion_model.EmotionModel.predict")
    def test_json_structure(self, mock_predict):
        mock_predict.return_value = (2, [[0.1, 0.1, 0.6, 0.1, 0.05, 0.05]])  # joy

        resp = self.client.get("/emotionDetector", query_string={"textToAnalyze": "I love this"})
        data = resp.get_json()

        self.assertIn("text", data)
        self.assertIn("emotion", data)
        self.assertIn("probabilities", data)
        self.assertIsInstance(data["probabilities"], list)
        self.assertEqual(len(data["probabilities"][0]), 6)

    # ---------------------------
    # POST INVALID JSON
    # ---------------------------
    def test_post_invalid_json(self):
        resp = self.client.post(
            "/emotionDetector",
            data="not-json",
            content_type="application/json"
        )
        self.assertIn(resp.status_code, (400, 415))

    # ---------------------------
    # POST MISSING FIELD
    # ---------------------------
    def test_post_missing_field(self):
        resp = self.client.post(
            "/emotionDetector",
            data=json.dumps({}),
            content_type="application/json"
        )
        self.assertEqual(resp.status_code, 400)

        data = resp.get_json()
        self.assertIn("error", data)


if __name__ == "__main__":
    unittest.main()
