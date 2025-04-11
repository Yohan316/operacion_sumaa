import unittest
from operacionesaritmeticas import OperacionesAritmeticas



class TestSuma(unittest.TestCase):
    def test_suma_dosNumeeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = OperacionesAritmeticas(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado,resultadoActual, "Falló la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(3, "a")
        with self.assertRaises(TypeError):
                objSuma.calcularSuma()

    def test_division_dosNumeeros_retornaDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15

        resultadoEsperado = 0.666

        objSuma = OperacionesAritmeticas(dividendo, divisor)

        # Act

        resultadoActual = objSuma.calcularDivision()

        # Assert
        self.assertAlmostEqual(resultadoEsperado,resultadoActual, 2 ,"Falló la división")



if __name__ == '__main__':
    unittest.main()
import unittest
from division import Division

class TestDivision(unittest.TestCase):
    def test_division_dosNumeros_retornaResultado(self):
        # Arrange
        dividendo = 20
        divisor = 4
        resultadoEsperado = 5

        objDivision = Division(dividendo, divisor)

        # Act
        resultadoActual = objDivision.calcularDivision()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, "Falló la división")

    def test_division_porCero_lanzaExcepcion(self):
        # Arrange
        objDivision = Division(10, 0)

        # Assert
        with self.assertRaises(ZeroDivisionError):
            objDivision.calcularDivision()

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        # Arrange
        objDivision = Division(10, "a")

        # Assert
        with self.assertRaises(TypeError):
            objDivision.calcularDivision()

if __name__ == '__main__':
    unittest.main()
