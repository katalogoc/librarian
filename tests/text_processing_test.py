import unittest
import src.text_processing as proc

class TestContentFraction(unittest.TestCase):
    def test_calculates_content_fraction(self):
        self.assertEqual(
            proc.content_fraction(['an', 'a', 'the']),
            0
        )
        self.assertEqual(
            proc.content_fraction(['You', 'are', 'lovin\'', 'it']),
            0.25
        )
        self.assertEqual(
            proc.content_fraction(['Gold', 'Silver', 'Coffee', 'it']),
            0.75
        )
        self.assertEqual(
            proc.content_fraction(['Desk']),
            1
        )

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
            proc.tokenize_money_dates_names_and_organizations('yet another $1'),
            ['$1']
        )

    def test_tokenizes_percentage_values(self):
        self.assertEqual(
            proc.tokenize_money_dates_names_and_organizations('1% and 2%'),
            ['1%', '2%']
        )

    def test_tokenizes_names(self):
        self.assertEqual(
            proc.tokenize_money_dates_names_and_organizations('John loves Katty'),
            ['John', 'Katty']
        )

class hAck3r(unittest.TestCase):
    def test_converts_to_hAck3r_string(self):
        self.assertEqual(
            proc.hAck3r('We elders, who in the storms of the age have ripened into men.'),
            'W3 3|d3r5, wh0 1n th3 5t0rm5 0f th3 ag3 hav3 r1p3n3d 1nt0 m3n5w33t!'
        )

if __name__ == '__main__':
    unittest.main()
