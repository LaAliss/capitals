import unittest
import sys
from CapitalsFolder.capitals import get_capital
from CapitalsFolder.capitals import get_state
from CSVfolder.csvcode import get_capital_or_state
import os


class TestCapitals(unittest.TestCase):

    def setUp(self):
        self.valid_capital = 'Rome'
        self.invalid_capital = 'Napoli'
        self.valid_state = 'Italy'
        self.invalid_state = 'Cambogia'

    '''
    This function check if there exists the CSV file

    '''

    def test_check_path(self):
        self.assertFalse(os.path.exists("data/invented_file.csv"))

    '''
    This function checks if the function works whenever
    I use a correct input for capital.
    '''

    def test_capital_valid(self):
        self.assertEqual('Italy', get_capital(self.valid_capital))

    '''
    This function checks if the function works
    whenever I use an incorrect input for capital.

    '''

    def test_capital_invalid(self):
        self.assertEqual('', get_capital(self.invalid_capital))

    '''
    This function checks if the function works whenever
    I use a correct input for State.

    '''

    def test_state_valid(self):
        self.assertEqual('Rome', get_state(self.valid_state))

    '''
    This function checks if the function works whenever
    I use an incorrect input for State.

    '''

    def test_state_invalid(self):
        self.assertEqual('', get_state(self.invalid_state))


class TestCsv(unittest.TestCase):

    def test_capital_or_state_valid(self):
        state = 'Italy'
        self.assertEqual('Rome', get_capital_or_state(state))

    def test_capital_or_state_invalid(self):
        state = 'Cambogia'
        self.assertEqual(None, get_capital_or_state(state))


if __name__ == '__main__':
    unittest.main()
