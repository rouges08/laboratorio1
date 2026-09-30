class RegistroVoti:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def __str__(self):
        return f"Voti: {self.voti}"


if __name__ == "__main__":
    registro = RegistroVoti()
    registro.aggiungi_voto(7)
    registro.aggiungi_voto(8)
    print(registro)