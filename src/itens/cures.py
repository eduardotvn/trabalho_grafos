from models import Cure

class PocaoPequena(Cure):
    NAME = 'Poção Pequena'
    DESCRIPTION = 'Um pequeno frasco contendo um líquido de propriedades curativas, feito com plantas da ilha.'
    USABILITY = 1
    HEAL = 10
    def __init__(self):
        super().__init__(PocaoPequena.NAME, PocaoPequena.DESCRIPTION, PocaoPequena.USABILITY, PocaoPequena.HEAL)
        
class PocaoMedia(Cure):
    NAME = 'Poção Média'
    DESCRIPTION = 'Um frasco contendo um líquido de propriedades curativas, feito com plantas da ilha.'
    USABILITY = 2
    HEAL = 10
    def __init__(self):
        super().__init__(PocaoMedia.NAME, PocaoMedia.DESCRIPTION, PocaoMedia.USABILITY, PocaoMedia.HEAL)
    
class PocaoGrande(Cure):
    NAME = 'Poção Grande'
    DESCRIPTION = 'Um grande frasco contendo um líquido de propriedades curativas, feito com plantas da ilha.'
    USABILITY = 3
    HEAL = 10
    def __init__(self):
        super().__init__(PocaoGrande.NAME, PocaoGrande.DESCRIPTION, PocaoGrande.USABILITY, PocaoGrande.HEAL)
  