from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        cases = [
            {'statement': 'I am glad this happened', 'dom': 'joy'},
            {'statement':'I am really mad about this', 'dom': 'anger'},
            {'statement':'I feel disgusted just hearing about this', 'dom': 'disgust'},
            {'statement':'I am so sad about this', 'dom': 'sadness'},
            {'statement':'I am really afraid that this will happen', 'dom': 'fear'}
        ]
        for case in cases:
            emotions = emotion_detector(case['statement'])
            self.assertEqual(emotions['dominant_emotion'], case['dom'])
        
unittest.main()
