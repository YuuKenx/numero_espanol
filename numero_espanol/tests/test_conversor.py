import unittest
from numero_espanol.conversor import convertir

class TestConversor(unittest.TestCase):
    def test_convertir_unidades(self):
        self.assertEqual(convertir("uno"), 1)
        self.assertEqual(convertir("dos"), 2)
        self.assertEqual(convertir("tres"), 3)
        self.assertEqual(convertir("cuatro"), 4)
        self.assertEqual(convertir("cinco"), 5)
        self.assertEqual(convertir("seis"), 6)
        self.assertEqual(convertir("siete"), 7)
        self.assertEqual(convertir("ocho"), 8)
        self.assertEqual(convertir("nueve"), 9)

    def test_convertir_decenas(self):
        self.assertEqual(convertir("diez"), 10)
        self.assertEqual(convertir("once"), 11)
        self.assertEqual(convertir("doce"), 12)
        self.assertEqual(convertir("trece"), 13)
        self.assertEqual(convertir("catorce"), 14)
        self.assertEqual(convertir("quince"), 15)
        self.assertEqual(convertir("dieciséis"), 16)
        self.assertEqual(convertir("diecisiete"), 17)
        self.assertEqual(convertir("dieciocho"), 18)
        self.assertEqual(convertir("diecinueve"), 19)
        self.assertEqual(convertir("veinte"), 20)
        self.assertEqual(convertir("veintiuno"), 21)
        self.assertEqual(convertir("veintidós"), 22)
        self.assertEqual(convertir("treinta"), 30)
        self.assertEqual(convertir("treinta y uno"), 31)
        self.assertEqual(convertir("cuarenta y dos"), 42)
        self.assertEqual(convertir("cincuenta y tres"), 53)
        self.assertEqual(convertir("sesenta y cuatro"), 64)
        self.assertEqual(convertir("setenta y cinco"), 75)
        self.assertEqual(convertir("ochenta y seis"), 86)
        self.assertEqual(convertir("noventa y siete"), 97)

    def test_convertir_centenas(self):
        self.assertEqual(convertir("cien"), 100)
        self.assertEqual(convertir("ciento uno"), 101)
        self.assertEqual(convertir("ciento diez"), 110)
        self.assertEqual(convertir("ciento veinte"), 120)
        self.assertEqual(convertir("ciento treinta y dos"), 132)
        self.assertEqual(convertir("doscientos"), 200)
        self.assertEqual(convertir("doscientos uno"), 201)
        self.assertEqual(convertir("trescientos cuarenta y cinco"), 345)
        self.assertEqual(convertir("cuatrocientos cincuenta y seis"), 456)
        self.assertEqual(convertir("quinientos sesenta y siete"), 567)
        self.assertEqual(convertir("seiscientos setenta y ocho"), 678)
        self.assertEqual(convertir("setecientos ochenta y nueve"), 789)
        self.assertEqual(convertir("ochocientos noventa"), 890)
        self.assertEqual(convertir("novecientos noventa y nueve"), 999)

    def test_convertir_mil(self):
        self.assertEqual(convertir("mil"), 1000)
        self.assertEqual(convertir("mil uno"), 1001)
        self.assertEqual(convertir("mil cien"), 1100)
        self.assertEqual(convertir("mil doscientos treinta y cuatro"), 1234)
        self.assertEqual(convertir("dos mil"), 2000)
        self.assertEqual(convertir("tres mil cuatrocientos cincuenta y seis"), 3456)
        self.assertEqual(convertir("diez mil"), 10000)
        self.assertEqual(convertir("once mil ciento once"), 11111)
        self.assertEqual(convertir("novecientos noventa y nueve mil novecientos noventa y nueve"), 999999)

    def test_convertir_millon(self):
        self.assertEqual(convertir("un millón"), 1000000)
        self.assertEqual(convertir("dos millones"), 2000000)
        self.assertEqual(convertir("un millón uno"), 1000001)
        self.assertEqual(convertir("un millón cien"), 1000100)
        self.assertEqual(convertir("un millón ciento uno"), 1000101)
        self.assertEqual(convertir("un millón doscientos treinta y cuatro"), 1000234)
        self.assertEqual(convertir("dos millones trescientos cuarenta y cinco mil seiscientos setenta y ocho"), 2345678)

if __name__ == '__main__':
    unittest.main()