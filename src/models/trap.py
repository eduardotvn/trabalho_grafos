from random import choices

class Trap():

    def __init__(self, name: str, description: str, damage: int, dangerProbability: float) -> None:
        if dangerProbability > 1 or dangerProbability < 0:
            raise ValueError('The danger probability must be in the interval [0, 1]')
        self.__name = name
        self.__description = description
        self.__dangerProbability = dangerProbability
        self.__damage = damage

    def getDamage(self) -> int:
        """
        Retorna do dano da armadilha.
        """
        return self.__damage
    
    def getDangerProbability(self) -> float:
        """
        Retorna a probabilidade da armadilha estar ativa.
        """
        return self.__dangerProbability
    
    def getName(self) -> str:
        """
        Retorna o nome da armadilha.
        """
        return self.__name
    
    def getDescription(self) -> str:
        """
        Retorna uma descrição da armadilha.
        """
        return self.__description
    
    def active(self) -> bool:
        """
        Retorna se a armadilha está ativa ou não.\n
        Esse valor depende da probabilidade de perigo.
        """
        return choices([True, False], weights=[self.getDangerProbability(), 1 - self.getDangerProbability()])[0]

