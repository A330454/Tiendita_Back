class Carro:
    llantas = 4
    puertas = 4
    motor = 1
    velocidad = 120

    def avanzar(self):
        print("estoy avanzando a: " + str(self.velocidad))
    
if __name__ == "__main__":
    x = Carro()
    x.avanzar()
    x.velocidad = 150
    x.avanzar()