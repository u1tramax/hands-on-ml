from abc import ABC, abstractmethod

# --------- Стратегия ---------
class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate(self, weight: float) -> float:
        # TODO: метод должен вычислять цену в зависимости от веса
        pass


# --------- Конкретные стратегии ---------

class CourierDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        # TODO: вернуть цену: базовая ставка 200 + 20 за каждый кг
        return 200 + weight * 20


class PostDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        # TODO: вернуть цену: 100 + 10 за каждый кг
        return 100 + weight * 10


class AirDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        # TODO: вернуть цену: 500 + 50 за каждый кг
        return 500 + weight * 50


# --------- Контекст ---------
class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        # TODO: сохранить стратегию в поле объекта
        self.strategy = strategy
    
    def set_strategy(self, strategy: DeliveryStrategy):
        # TODO: сменить стратегию
        self.strategy = strategy
    
    def calculate_price(self, weight: float):
        # TODO: вызвать метод стратегии
        return self.strategy.calculate(weight)


# --------- Тест ---------

# TODO: создайте контекст с любой стратегией
context = DeliveryContext(CourierDelivery())

# TODO: посчитайте стоимость посылки весом 3 кг
print(context.calculate_price(3))

# TODO: смените стратегию и посчитайте снова
context.set_strategy(AirDelivery())

# TODO: выведите результаты
print(context.calculate_price(3))