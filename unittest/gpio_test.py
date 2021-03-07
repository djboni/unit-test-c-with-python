#!/usr/bin/python3
from load_c import load
import unittest, unittest.mock

class GPIOTest(unittest.TestCase):
  def setUp(self):
    self.module, self.ffi = load('gpio')
  
  def test_read_gpio0(self):
    @self.ffi.def_extern()
    def read_gpio0():
      return 42
    self.assertEqual(self.module.read_gpio(0), 42)
  
  def test_read_gpio1(self):
    read_gpio1 = unittest.mock.MagicMock(return_value=21)
    self.ffi.def_extern('read_gpio1')(read_gpio1)
    self.assertEqual(self.module.read_gpio(1), 21)
    read_gpio1.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
