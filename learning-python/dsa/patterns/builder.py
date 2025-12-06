class Burger:
    def __init__(self):
        self.bun = None
        self.meat = None
        self.sauce = None
        self.vegetables = []

    def __str__(self):
        return (
            f"Burger("
            f"bun={self.bun}, "
            f"meat={self.meat}, "
            f"sauce={self.sauce}, "
            f"vegetables={self.vegetables}"
            f")"
        )

class BurgerBuilder:
    """
    Абстрактный строитель.
    Определяет шаги, которые должен реализовать конкретный строитель.
    """

    def reset(self):
        """Создать новый пустой бургер"""
        return Burger()

    def set_bun(self, bun: str):
        # TODO: установить булку
        self.bun = bun

    def set_meat(self, meat: str):
        # TODO: установить мясо
        self.meat = meat

    def set_sauce(self, sauce: str):
        # TODO: установить соус
        self.sauce = sauce

    def add_vegetable(self, vegetable: str):
        # TODO: добавить овощ
        self.vegetable = vegetable

    def get_result(self) -> Burger:
        """
        Вернуть построенный объект.
        """
        # TODO: вернуть объект, который строитель создавал
        return Burger().set_bun().set_meat().set_sauce()


# -----------------------
# CONCRETE BUILDER
# -----------------------

class ClassicBurgerBuilder(BurgerBuilder):
    """
    Конкретный строитель "классического" бургера.
    """

    def __init__(self):
        self.reset()

    # TODO: реализовать все пустые методы из базового класса


# -----------------------
# DIRECTOR
# -----------------------

class BurgerDirector:
    """
    Директор — определяет порядок шагов для разных вариантов бургеров.
    """

    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def make_classic_burger(self):
        """
        Собрать классический бургер:
        булка, мясо, салат, помидор, соус
        """
        # TODO: вызвать методы билдера в нужном порядке


# -----------------------
# TEST
# -----------------------

builder = ClassicBurgerBuilder()
director = BurgerDirector(builder)

# Собираем классический бургер
director.make_classic_burger()
burger = builder.get_result()
print(burger)

# Можно собрать другой бургер вручную:
builder.reset()
builder.set_bun("sesame")
builder.set_meat("chicken")
builder.add_vegetable("onion")
builder.add_vegetable("peper")
print(builder.get_result())
