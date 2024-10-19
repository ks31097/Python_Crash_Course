import unittest
from survey import AnonymousServey

class TestAnonmyousServey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Checks that one answer is saved correctly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousServey(question)
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)

    def test_store_three_responses(self):
        """Checks that the three answers were saves correctly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousServey(question)
        responses = ["English", "Spanish", "Mandarin"]
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()