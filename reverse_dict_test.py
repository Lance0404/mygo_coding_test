import unittest
from reverse_dict import *


class TestReverseDict(unittest.TestCase):
  def setUp(self) -> None:
    
    self.input_1 = {
      'hired': {
        'be': {
          'to': {
            'deserve': 'I'
          }
        }
      }
    }

    self.output_1 = {
      'I': {
        'deserve': {
          'to': {
            'be': 'hired'
          }
        }
      }
    }

    self.input_2 = {
      'hired': 'me'
    }

    self.output_2 = {
      'me': 'hired'
    }

    self.input_3 = 'hired'

  def tearDown(self) -> None:
    pass

  def test_reverse_dict_case_1(self):
    print(f'start running function: {self._testMethodName}')
    result = reverse_dict(self.input_1)
    self.assertIsInstance(result, dict)
    self.assertEqual(result, self.output_1)
    print(f'finished running function: {self._testMethodName}')

  def test_reverse_dict_case_2(self):
    print(f'start running function: {self._testMethodName}')
    result = reverse_dict(self.input_2)
    self.assertIsInstance(result, dict)
    self.assertEqual(result, self.output_2)
    print(f'finished running function: {self._testMethodName}')

  def test_reverse_dict_case_3(self):
    print(f'start running function: {self._testMethodName}')
    self.assertRaises(UnmatchException, reverse_dict, self.input_3)
    print(f'finished running function: {self._testMethodName}')


if __name__ == '__main__':
    unittest.main()

