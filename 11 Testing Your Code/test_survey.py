import unittest
from survey import AnonymousSurvey


class TestAnonyomousSurvey(unittest.TestCase):
    """Tests for AnonymousSurvey."""

    def test_store_single_response(self):
        """Tests that a single response is stored properly."""
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)

        my_survey.store_response("English")
        self.assertIn(
            "English", my_survey.responses
        )  # assertIn allows us to see if an item is in a list.

    def test_store_three_responses(self):
        """Test that three individual responses are stored correctly."""
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)

        responses = ["english", "spanish", "mandarin"]
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()

# This works perfectly. However, these tests are a bit repetitive,
# so we’ll use another feature of unittest to make them more efficient.
# can be seen on test_survey_2.py

