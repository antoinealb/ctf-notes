#!/usr/bin/env python3
import unittest
from pattern import *
class PatternGeneratorTestCase(unittest.TestCase):
    def test_can_generate_first_letter(self):
        self.assertEqual('A', next(generate_pattern()))

    def test_generate_simple_pattern(self):
        g = generate_pattern()
        self.assertEqual('A', next(g))
        self.assertEqual('a', next(g))
        self.assertEqual('1', next(g))

    def test_char_range(self):
        c = len(list(char_range('a', 'z')))
        self.assertEqual(26, c)

    def test_middle_letter_change(self):
        g = generate_pattern()

        for i in range(1, 10):
            self.assertEqual('A', next(g))
            self.assertEqual('a', next(g))
            self.assertEqual(str(i), next(g))

        self.assertEqual('A', next(g))
        self.assertEqual('b', next(g))
        self.assertEqual('1', next(g))

    def test_start_letter_change(self):
        g = generate_pattern()

        a, _, _ = next(g), next(g), next(g)
        while a == 'A':
            a, _, _ = next(g), next(g), next(g)

        self.assertEqual(a, 'B')

class PatternMatcherTestCase(unittest.TestCase):
    def test_can_convert_adress_to_pattern(self):
        adress = "0x41424344"
        pattern = adress_to_pattern(adress)
        self.assertEqual(['D', 'C', 'B', 'A'], pattern)

    def test_can_convert_adress_to_pattern(self):
        adress = "0x41424344"
        pattern = adress_to_pattern(adress, big_endian=True)
        self.assertEqual(['A', 'B', 'C', 'D'], pattern)

    def test_can_match_start_pattern(self):
        adress = "0x41316141"
        pattern = adress_to_pattern(adress)
        self.assertEqual(['A', 'a', '1', 'A'], pattern)
        offset = find_offset(pattern)
        self.assertEqual(0, offset)

    def test_can_match_more_complex_pattern(self):
        pattern = ['1', 'A', 'a', '2']
        offset = find_offset(pattern)
        self.assertEqual(2, offset)

if __name__ == "__main__":
    unittest.main()
