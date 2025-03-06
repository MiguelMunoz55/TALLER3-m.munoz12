import unittest
from app.models.huron import Huron
from app.models.boaconstrictor import BoaConstrictor

class TestAnimales(unittest.TestCase):

    def test_huron_sonido(self):
        h = Huron(nombre="Huron de prueba")
        self.assertEqual(h.hacer_sonido(), "¡Eek Eek!")

    def test_boa_sonido(self):
        b = BoaConstrictor(nombre="Boa de prueba")
        self.assertEqual(b.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        h = Huron(nombre="Huron de prueba")
        b = BoaConstrictor(nombre="Boa de prueba")
        self.assertAlmostEqual(h.calcular_flete(100, 0.1), 10)
        self.assertAlmostEqual(b.calcular_flete(200, 0.2), 40)

    def test_alimentar_boa(self):
        b = BoaConstrictor(nombre="Boa de prueba", ratones_comidos=0)
        
        for _ in range(9):
            self.assertEqual(b.alimentar(), "Alimentado")
        
        print(f"Ratones comidos antes del décimo intento: {b.ratones_comidos}")

        try:
            b.alimentar()
            self.fail("No se lanzó ValueError cuando la boa comió 10 ratones.")
        except ValueError as e:
            self.assertEqual(str(e), "Demasiados Ratones!")

class Guarderia:
    def __init__(self, boas, hurones):
        self.boas = boas
        self.hurones = hurones

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.alimentar()
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"

class TestGuarderia(unittest.TestCase):
    def test_alimentar_boa(self):
        # Caso en que la boa puede alimentarse (menos de 10 ratones consumidos)
        b1 = BoaConstrictor(nombre="Boa 1", ratones_comidos=5)
        g = Guarderia([b1], [])
        self.assertEqual(g.alimentar_boa(b1), "Éxito")
        
        # Caso donde la boa ya está llena (10 o más ratones consumidos)
        b2 = BoaConstrictor(nombre="Boa 2", ratones_comidos=10)
        g.boas.append(b2)  
        self.assertEqual(g.alimentar_boa(b2), "La boa está llena")
        
        # Caso en que la boa es None
        self.assertEqual(g.alimentar_boa(None), "Esta Boa no existe!")

if __name__ == '__main__':
    unittest.main()