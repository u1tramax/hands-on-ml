# --------- Подсистема 1 ---------
class LightSystem:
    def turn_on(self):
        print("Свет включён")

    def turn_off(self):
        print("Свет выключен")


# --------- Подсистема 2 ---------
class MusicSystem:
    def play_music(self):
        print("Музыка играет")

    def stop_music(self):
        print("Музыка остановлена")


# --------- Подсистема 3 ---------
class ClimateSystem:
    def set_temperature(self, temp: float):
        print(f"Температура установлена на {temp}°C")

    def turn_off(self):
        print("Климат-контроль выключен")


# --------- ФАСАД ---------
class SmartHomeFacade:
    def __init__(self):
        # TODO: Создать все подсистемы (сохранить их в полях)
        self.light = LightSystem()
        self.music = MusicSystem()
        self.climate = ClimateSystem()

    def start_party_mode(self):
        # TODO: включить свет
        # TODO: включить музыку
        # TODO: установить температуру 22°C
        self.light.turn_on()
        self.music.play_music()
        self.climate.set_temperature(22)

    def leave_home_mode(self):
        # TODO: выключить свет
        # TODO: остановить музыку
        # TODO: выключить климат
        self.light.turn_off()
        self.music.stop_music()
        self.climate.turn_off()


# --------- ТЕСТ ---------

# TODO: создать объект фасада
smarthome = SmartHomeFacade()

# TODO: включить режим вечеринки
smarthome.start_party_mode()

# TODO: включить режим ухода
smarthome.leave_home_mode()
