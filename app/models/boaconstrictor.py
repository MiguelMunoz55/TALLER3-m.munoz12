from app.config.db import db

class BoaConstrictor(db.Model):
    __tablename__ = "boas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    ratones_comidos = db.Column(db.Integer, default=0, nullable=False)

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def calcular_flete(self, peso: float, impuestos: float) -> float:
        return peso * impuestos

    def alimentar(self) -> str:
        if self.ratones_comidos is None:
            self.ratones_comidos = 0

        if self.ratones_comidos >= 9:
            raise ValueError("Demasiados Ratones!")
        
        self.ratones_comidos += 1

        return "Alimentado"