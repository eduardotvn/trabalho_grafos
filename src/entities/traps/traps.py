from models import Trap

class AreiaMovedica(Trap):
    NAME = 'Areia Movediça'
    DESCRIPTION = 'O chão parece querer te conhecer melhor'
    DANGER = .7
    DAMAGE = 5

    def __init__(self) -> None:
        super().__init__(AreiaMovedica.NAME, AreiaMovedica.DESCRIPTION, AreiaMovedica.DAMAGE, AreiaMovedica.DANGER)

class CaminhoIngreme(Trap):
    NAME = 'Caminho Íngreme'
    DESCRIPTION = 'Você se fere tentando escalar uma estrada íngreme'
    DANGER = .9
    DAMAGE = 2

    def __init__(self) -> None:
        super().__init__(CaminhoIngreme.NAME, CaminhoIngreme.DESCRIPTION, CaminhoIngreme.DAMAGE, CaminhoIngreme.DANGER)

class PlantaCarnivora(Trap):
    NAME = 'Planta Carnívora Gigante'
    DESCRIPTION = 'Uma planta carnívora acaba de ti confundir com inceto'
    DANGER = .4
    DAMAGE = 10

    def __init__(self) -> None:
        super().__init__(PlantaCarnivora.NAME, PlantaCarnivora.DESCRIPTION, PlantaCarnivora.DAMAGE, PlantaCarnivora.DANGER)
