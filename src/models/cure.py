from item import Item
from explorator import Explorator

class Cure(Item):
    def __init__(self, usability, heal) -> None:
        super().__init__()
        self.__usability = usability
        self.__heal = heal
        
    def getUsability(self) -> int:
        return self.__usability
    
    def getHeal(self) -> int:
        if self.__usability > 0:
            return self.__heal
        
    def use(self, explorator: Explorator) -> None:
        if self.__usability > 0:
            self.__usability -= 1
            explorator.setHeal(self.getHeal())
            
    def tostring(self) -> str:
        return f'Cure: [Heal: {self.getHeal()}, Usability: {self.getUsability()}]'