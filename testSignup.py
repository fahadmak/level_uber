import unittest
from signup import *

class SignUpTestCase(unittest.TestCase):
    def setUp(self):
        self.sign = SignUp('fahad', 'makabugo','f.faraqhan@gmail.com')
    
    def test_full_name(self):
        self.assertEqual(self.sign.combined_name('fahad', 'makabugo'), 'fahad makabugo')
    
    def test_validate_email(self):
        self.assertEqual(self.sign.validate_email('f.faraqhan@gmail.com'), 'f.faraqhan@gmail.com')


if __name__ == '__main__':
    unittest.main()
