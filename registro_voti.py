class RegistroVoti:
    def __init__(self, soglia_sufficienza=6):
        self.voti = []
        self.soglia_sufficienza = soglia_sufficienza

    def aggiungi_voto(self, voto):
        if not isinstance(voto, (int, float)):
            raise TypeError("Il voto deve essere un numero")
        if not 0 <= voto <= 10:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")
        self.voti.append(voto)

    def rimuovi_voto(self, voto):
        """Rimuove la prima occorrenza del voto indicato."""
        try:
            self.voti.remove(voto)
        except ValueError:
            raise ValueError(f"Il voto {voto} non è presente nel registro")

    def media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def mediana(self):
        if not self.voti:
            return None
        ordinati = sorted(self.voti)
        n = len(ordinati)
        meta = n // 2
        if n % 2 == 0:
            return (ordinati[meta - 1] + ordinati[meta]) / 2
        return ordinati[meta]

    def voto_massimo(self):
        return max(self.voti) if self.voti else None

    def voto_minimo(self):
        return min(self.voti) if self.voti else None

    def voti_sufficienti(self):
        return [v for v in self.voti if v >= self.soglia_sufficienza]

    def e_promosso(self):
        return self.media() >= self.soglia_sufficienza

    def __len__(self):
        return len(self.voti)

    def __str__(self):
        return f"Voti: {self.voti} (totale: {len(self)})"


if __name__ == "__main__":
    registro = RegistroVoti()
    registro.aggiungi_voto(7)
    registro.aggiungi_voto(8)
    registro.aggiungi_voto(5)
    registro.aggiungi_voto(9)

    print(registro)
    print("Media:", registro.media())
    print("Mediana:", registro.mediana())
    print("Voto massimo:", registro.voto_massimo())
    print("Voto minimo:", registro.voto_minimo())
    print("Voti sufficienti:", registro.voti_sufficienti())
    print("Promosso:", registro.e_promosso())

    registro.rimuovi_voto(5)
    print("Dopo la rimozione:", registro)

    try:
        registro.aggiungi_voto(11)
    except ValueError as e:
        print("Errore:", e)