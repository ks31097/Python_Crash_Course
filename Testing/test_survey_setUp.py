import unittest
from survey import AnonymousServey

class TestAnonmyousServey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def setUp(self):
        """Create a survey and set of answers for all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousServey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Checks that one answer is saved correctly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Checks that the three answers were saves correctly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()