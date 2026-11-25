class veiculos:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max


    def mover(self):
        print(f"O veículo da marca {self.marca} está se movendo a uma velocidade máxima de {self.velocidade_max} km/h.")


class Carro(veiculos):
    def __init__(self, marca, velocidade_max, portas):
        super().__init__(marca, velocidade_max)
        self.portas = portas


    def descricao(self):
        print(
            f"Marca: {self.marca}\n"
            f"Velocidade Máxima: {self.velocidade_max} km/h\n"
            f"Número de Portas: {self.portas}"
        )


    def mover(self):
        print(f"O carro da marca {self.marca} está se movendo a uma velocidade máxima de {self.velocidade_max} km/h.")




class bicicleta(veiculos):
    def __init__(self, marca, num_marchas, velocidade_max, tipo):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas
        self.tipo = tipo


    def descricao(self):
        print(
            f"Marca: {self.marca}\n"
            f"Velocidade Máxima: {self.velocidade_max} km/h\n"
            f"Número de Marchas: {self.num_marchas}\n"
            f"Tipo: {self.tipo}"
        )


    def mover(self):
        print(f"A bicicleta da marca {self.marca} está se movendo a uma velocidade máxima de {self.velocidade_max} km/h.")


bicicleta1 = bicicleta("Caloi", 21, 30, "Mountain Bike")
bicicleta1.descricao()
bicicleta1.mover()
carro1 = Carro("Toyota", 180, 4)
carro1.descricao()
carro1.mover()