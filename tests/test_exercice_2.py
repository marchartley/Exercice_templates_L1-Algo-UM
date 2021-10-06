import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_2 as TP
import nose2
import unittest

class Test_Exercice2_ManipSurNombres(unittest.TestCase):
    def test_nombre_de_chiffres(self):
        self.assertEqual(TP.nbChifDec(123456789), 9)
        self.assertEqual(TP.nbChifDec(1), 1)

    def test_rang_d_un_nombre(self):
        self.assertEqual(TP.chifRang(456789, 2), 8)
        self.assertEqual(TP.chifRang(99, 3), 0)

    def test_somme_des_chiffres(self):
        self.assertEqual(TP.somChif(1234), 10)
        self.assertEqual(TP.somChif(7895426), 41)

    def test_racine_numerique(self):
        self.assertEqual(TP.racineNumerique(1234), 1)
        self.assertEqual(TP.racineNumerique(7895426), 5)
        self.assertEqual(TP.racineNumerique(9999999999), 9)

    def test_inversion_nombre(self):
        self.assertEqual(TP.invChif(123456), 654321)
        self.assertEqual(TP.invChif(5), 5)

if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 2...")
    nose2.main()
