import pandas as pd

class Test(unittest.TestCase):

  def test_cinemas_maiores_é_um_dataFrame(self):
    self.assertEquals(type(cinemas_maiores), pd.DataFrame)
    
  def test_cinemas_maiores_tem_três_linhas(self):
    self.assertEquals(len(cinemas_maiores), 3)   
    
  def test_cinemas_maiores_contém_o_maior_cinemas(self):
    seats = list(cinemas_maiores["seats"])
    self.assertTrue(1107 in seats, "Contém o maior cinema")
    self.assertTrue(969 in seats, "Contém o segundo maior cinema")
    self.assertTrue(914 in seats, "Contém o terceiro maior cinema")