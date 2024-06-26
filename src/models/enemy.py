from .creature import Creature


class Enemy(Creature):
    """
    Classe de inimigos que podem ser enfrentados pelo jogador.
    """
    def __init__(self, hp: int, attack: int, name: str, description: str):
        super().__init__(hp, attack, name, description)
