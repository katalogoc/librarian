import unittest
import src.text_processing as proc

class TestStripDeterminers(unittest.TestCase):
    def test_strips_determiners_when_determiner_is_a_part_of_the_word(self):
            self.assertEqual(
                proc.strip_determiners('Breaking News: The Guardian magazine has posted a tweet about the climate crisis therefore it is a popular topic'),
                'Breaking News: Guardian magazine has posted tweet about climate crisis therefore it is popular topic'
            )

    def test_strips_determiners_case_insensetively(self):
            self.assertEqual(
                proc.strip_determiners('YOU HAVE AN HOUR AND A MINUTE'),
                'YOU HAVE HOUR AND MINUTE'
            )

    def test_strips_determiners_in_a_string_beginning_with_determiner(self):
            self.assertEqual(
                proc.strip_determiners('An elephant and a beaver are the greatest animals'),
                'elephant and beaver are greatest animals'
            )


if __name__ == '__main__':
    unittest.main()
    