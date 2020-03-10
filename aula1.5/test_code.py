import unittest

from code import listaMaiorElem

class TestListaMaiorElem(unittest.TestCase):
  def test_list_int(self):
    data = [1,5,3,9,0,11,2,3,9]
    result = listaMaiorElem(data)
    self.assertEqual(result, 11)


if __name__ == "__main__":
    unittest.main()

