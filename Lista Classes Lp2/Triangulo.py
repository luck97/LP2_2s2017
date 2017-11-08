class Triangulo():
    def __init__(self, la, lb, lc):
        self.la = la
        self.lb = lb
        self.lc = lc
    
    def calcularPerimetro(self):
        return self.la + self.lb + self.lc

    def getMaior(self):
        return max([self.la, self.lb, self.lc])