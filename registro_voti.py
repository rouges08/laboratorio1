class RegistroVoti:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def voto_massimo(self):
        return max(self.voti) if self.voti else None

    def __str__(self):
        return f"Voti: {self.voti}"


if __name__ == "__main__":
    registro = RegistroVoti()
    registro.aggiungi_voto(7)
    registro.aggiungi_voto(8)
    print(registro)
    print("Media:", registro.media())
    print("Voto massimo:", registro.voto_massimo())