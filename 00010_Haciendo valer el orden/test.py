import pandas as pd

class Test(unittest.TestCase):

  def test_cines_mas_amplios_es_un_dataFrame(self):
    self.assertEquals(type(cines_mas_amplios), pd.DataFrame)
    
  def test_cines_mas_amplios_tiene_tres_filas(self):
    self.assertEquals(len(cines_mas_amplios), 3)   
    
  def test_cines_mas_amplios_contiene_los_cines_mas_amplios(self):
    seats = list(cines_mas_amplios["seats"])
    self.assertTrue(1107 in seats, "Contiene al cine más amplio")
    self.assertTrue(969 in seats, "Contiene al segundo cine más amplio")
    self.assertTrue(914 in seats, "Contiene al tercer cine más amplio")