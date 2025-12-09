#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


class Test_Question_C(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        """Test that the function returns the correct positions"""
        # Call the function with the sample parameters
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        
        # Unpack the result into individual variables
        pos1, pos2, pos3 = result
        
        # Test that each position is correct
        self.assertEqual(pos1, 2)
        self.assertEqual(pos2, 4)
        self.assertEqual(pos3, 10)
