from .item import Item

class Cure(Item):
    """
    Classe de itens de cura que podem ser usados pelo explorador.
    """

    def __init__(self, name: str, description: str, usability: int, heal: int) -> None:
        super().__init__(name, description, usability)
        self.__heal = heal
    
    def getHeal(self) -> int:
        """
        Retorna a informação do potencial de cura do item.
        """
        return self.__heal
        
    def use(self) -> int:
        """
        Serve para usar o item de cura.\n
        Retorna o potencial de cura do item.\n
        Leva em consideração a usabilidade.
        """
        if super().use():
            return self.getHeal()
        return 0
            
    def tostring(self) -> str:
        return f'Cure: [Heal: {self.getHeal()}, Usability: {self.getUsability()}]'
    