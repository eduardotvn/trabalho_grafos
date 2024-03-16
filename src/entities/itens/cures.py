from models import Cure

class CogumeloAngelical(Cure):
    NAME = 'Cogumelo Angelical'
    DESCRIPTION = 'Um cogumelo com um curioso formato de anjo, cresce apenas na ilha. Possui propriedades curativas.'
    USABILITY = 1
    HEAL = 10
    def __init__(self):
        super().__init__(CogumeloAngelical.NAME, CogumeloAngelical.DESCRIPTION, CogumeloAngelical.USABILITY, CogumeloAngelical.HEAL)
        
class PingoDaLua(Cure):
    NAME = 'Pingo da Lua'
    DESCRIPTION = 'Uma bela flor branca, contam as lendas que nasce quando uma gota de água cai da Lua. Possui propriedades curativas.'
    USABILITY = 1
    HEAL = 15
    def __init__(self):
        super().__init__(PingoDaLua.NAME, PingoDaLua.DESCRIPTION, PingoDaLua.USABILITY, PingoDaLua.HEAL)
    
class PomosDeOuro(Cure):
    NAME = 'Pomos de Ouro'
    DESCRIPTION = 'Uma fruta dourada, colhida do Jardim das Hespérides. Possui propriedades curativas.'
    USABILITY = 1
    HEAL = 20
    def __init__(self):
        super().__init__(PomosDeOuro.NAME, PomosDeOuro.DESCRIPTION, PomosDeOuro.USABILITY, PomosDeOuro.HEAL)
  