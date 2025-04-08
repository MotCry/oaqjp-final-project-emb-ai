import unittest


from EmotionDetection.emotion_detection import emotion_detector
class TestMyModule(unittest.TestCase):
    def test_detection(self):
        test_cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear'
        }
        for test, answer in test_cases.items():
            self.assertEqual(emotion_detector(test)['dominant_emotion'], answer)


unittest.main()