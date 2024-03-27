class Zawodnik:
    def __init__(self, imie, wzrost):
        self.imie = imie
        self.wzrost = wzrost
        
    def __repr__(self):
        return f"{self.imie} o wzoście {self.wzrost} cm"
    