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

class TestFindArithmeticExpressions(unittest.TestCase):
    def test_finds_simple_arithmetic_expression(self):
        self.assertEqual(
            proc.find_arithmetic_expressions('Teacher writes 2+2=4'),
            ['2+2=4']
        )

    def test_finds_all_arithmetic_expressions(self):
        self.assertEqual(
            proc.find_arithmetic_expressions('There were written 20+20=40, 40-40=0 and 30=30'),
            ['20+20=40', '40-40=0', '30=30']
        )

    def test_finds_arithmetic_expressions_when_whitespace_presents(self):
        self.assertEqual(
            proc.find_arithmetic_expressions('10 + 20=  30; 0/ 100=0'),
            ['10 + 20=  30', '0/ 100=0']
        )

class TestTokenize(unittest.TestCase):
    def test_tokenizes_money(self):
        self.assertEqual(
            proc.tokenize_money_dates_names_and_organizations('Banana costs $1'),
            ['$1']
        )

    def test_tokenizes_percentage_values(self):
        self.assertEqual(
            proc.tokenize_money_dates_names_and_organizations('Credit\'s annual percentage is 1%'),
            ['1%']
        )

if __name__ == '__main__':
    unittest.main()
    