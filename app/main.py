class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herb: 'Carnivore|Herbivore') -> None:
        if isinstance(herb, Carnivore):
            return
        if herb.hidden is False:
            herb.health -= 50
        if herb.health <= 0:
            herb.__class__.alive.remove(herb)
