class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        print(f"{self.marca} {self.modelo}: Freando...")

    def acelerar(self):
        print(f"{self.marca} {self.modelo}: Acelerando...")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self, porta):
        print (f"{self.marca} {self.modelo} : Abrindo porta {porta}...")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada, cor):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
        self.cor = cor

    def empinar(self):
        print (f"{self.marca} {self.modelo} : Empinando...")

carro = Carro("Fiat", "Uno", "Vermelho")
moto = Moto("Honda", "cg", "162,7 ", "azul")

print(f"Carro: {carro.marca} {carro.modelo} - Cor: {carro.cor}")
print(f"Moto: {moto.marca} {moto.modelo} - Cilindrada: {moto.cilindrada} - Cor: {moto.cor}")

carro.acelerar()
carro.frear()

moto.frear()
moto.acelerar()

moto.empinar()
carro.abrir_porta("as 4 portas")

