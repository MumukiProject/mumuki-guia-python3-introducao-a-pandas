class Test(unittest.TestCase):
  def setUp(self):
    self.maxDiff = None

  def test_primeira_livraria_é_um_Series(self):
    self.assertEquals(type(primeira_livraria), pd.Series)
    
  def test_segunda_e_terceira_livraria_é_um_DataFrame(self):
    self.assertEquals(type(segunda_e_terceira_livraria), pd.DataFrame)
        
  def test_última_livraria_é_um_Series(self):
    self.assertEquals(type(última_livraria), pd.Series)
    
  def test_primeira_livraria_tem_o_conteúdo_correto(self):
    self.assertEquals(primeira_livraria.to_json(), livraria.iloc[0].to_json())
    
  def test_segunda_e_terceira_livraria_tem_o_conteúdo_correto(self):
    self.assertEquals(segunda_e_terceira_livraria.to_json(), livraria.iloc[1:3].to_json())
        
  def test_última_livraria_tem_o_conteúdo_correto(self):
    self.assertEquals(última_livraria.to_json(), livraria.iloc[-1].to_json())
    
