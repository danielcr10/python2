import unittest

from code import *

class TestListaMaiorElem(unittest.TestCase):
  def test_list_int(self):
    data = [1,5,3,9,0,11,2,3,9]
    result = listaMaiorElem(data)
    self.assertEqual(result, 11)

  def test_list_float(self):
    data = [1,2,1.5,-4,7,-20,5.8]
    result = listaMaiorElem(data)
    self.assertEqual(result, 7)

  def test_list_float_only_negatives(self):
    data = [-1,-2,-1,-4,-7,-20,-5]
    result = listaMaiorElem(data)
    self.assertEqual(result, -1)


class TestListaSomaElem(unittest.TestCase):
  def test_list_int(self):
    data = [1,5,3,9,0,11,2,3,9]
    result = listaSomaElem(data)
    self.assertEqual(result, 43)

  def test_list_float(self):
    data = [1,2,1.5,-4,7,-20,5.8]
    result = listaSomaElem(data)
    self.assertEqual(result, -6.7)

  def test_list_float_only_negatives(self):
    data = [-1,-5,-3,-9,-0,-11,-2,-3,-9]
    result = listaSomaElem(data)
    self.assertEqual(result, -43)


class TestListaOcorPrimElem(unittest.TestCase):
  def test_list_all_different(self):
    data = [1,2,3,4,5,6,7,8,9,0,11]
    result = listaOcorPrimElem(data)
    self.assertEqual(result, 1)

  def test_list_all_equals(self):
    data = [0,0,0,0,0,00,0.0,0,0,0,0,0,0]
    result = listaOcorPrimElem(data)
    self.assertEqual(result, 13)
    
  def test_list_three_equals(self):
    data = [1,2,3,1,5,6,7,1,9,0,11]
    result = listaOcorPrimElem(data)
    self.assertEqual(result, 3)
    
  def test_list_floats(self):
    data = [1,2,3,4,-1,6,1,8,9,0,-11]
    result = listaOcorPrimElem(data)
    self.assertEqual(result, 2)

  def test_list_frist_negative(self):
    data = [-1,2,3,4,1,6,7,-1,9,0,11]
    result = listaOcorPrimElem(data)
    self.assertEqual(result, 2)
    
      
if __name__ == "__main__":
    unittest.main()

