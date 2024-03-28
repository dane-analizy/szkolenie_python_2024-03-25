import time


class Zawodnik:
    waga = 50

    def __init__(self, imie, wzrost):
        self.imie = imie
        self.wzrost = wzrost
        self.created = time.time()

    def __repr__(self):
        return f"{self.imie} o wzoście {self.wzrost} cm i wadze {self.waga}\nUtworzony w {self.created}."

    def get_waga(self):
        return self.waga

    def get_imie(self):
        return self.imie

    def get_wzrost(self):
        return self.wzrost

    def set_wzrost(self, w):
        self.wzrost = w

    @property
    def bmi(self):
        return self.waga / (self.wzrost / 100) ** 2

    @property
    def teraz(self):
        return time.time()


class Konfiguracja:
    kolor = "niebieski"
    rozmiar = 5
