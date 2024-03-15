from .item import Item

class Trap(Item):

    def __init__(self, name: str, description: str, usability: int, damage: int) -> None:
        super().__init__(name, description, usability)
        self.__damage = damage
    
    def getDamage(self) -> int:
        return self.__damage
    
    def use(self) -> int:
        return self.getDamage()
