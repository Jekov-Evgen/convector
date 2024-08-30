import unittest
from unittest.mock import patch
import sys
module_path = r'C:\Users\Женя\OneDrive\Desktop\программирование\чистое программирование\python\Currency_converter'
sys.path.append(module_path)
from Translation_functions import CurrencyTransfer

class TestCurrencyTransfer(unittest.TestCase):

    @patch('builtins.input', lambda *args: '-100')
    def test_negative_value(self):
        transfer = CurrencyTransfer()
        with self.assertRaises(ValueError):
            transfer.creating_a_window_from_hryvnia_to_dollars()
    
    
    
    
if __name__ == '__main__':
    unittest.main()