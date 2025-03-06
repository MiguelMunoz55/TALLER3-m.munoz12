from app.config.db import db

class Huron(db.Model):
    __tablename__ = "hurones"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"

    def calcular_flete(self, peso: float, impuestos: float) -> float:
        return peso * impuestos