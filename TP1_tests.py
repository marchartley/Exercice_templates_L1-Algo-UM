import TP1_template as TP
import nose2
import unittest
import sys, io
from contextlib import redirect_stdout

class Test_Exercice1_Binomes(unittest.TestCase):
    def test_calcul_binomial(self):
        self.assertEqual(TP.binome(5, 2), 10)
        self.assertEqual(TP.binome(10, 5), 252)

    def test_calcul_binomial_efficace(self):
        self.assertEqual(TP.binome_efficace(5, 2), 10)
        self.assertEqual(TP.binome_efficace(10, 5), 252)

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

class Test_Exercice3_SuiteDeSyracus(unittest.TestCase):
    def test_une_etape(self):
        self.assertEqual(TP.syracus(10), 5)
        self.assertEqual(TP.syracus(20), 10)
        self.assertEqual(TP.syracus(5), 16)

    def test_valeurs_suite(self):
        def check_suite(out, expected):
            out = [int(o) for o in out.getvalue().splitlines()]
            expected = [int(o) for o in expected]
            return out == expected

        f = io.StringIO()
        with redirect_stdout(f):
            TP.print_syracus(10)
        self.assertTrue(check_suite(f, [10, 5, 16, 8, 4, 2, 1]))

        f = io.StringIO()
        with redirect_stdout(f):
            TP.print_syracus(100)
        self.assertTrue(check_suite(f, [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]))

    def test_nombre_appels(self):
        self.assertEqual(TP.count_syracus(10), 6)
        self.assertEqual(TP.count_syracus(100), 25)

class Test_Exercice4_RechercheDansUneListe(unittest.TestCase):
    def test_recherche_sequentielle(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheSequentielle(arr, len(arr), 100), 7)
        self.assertEqual(TP.rechercheSequentielle(arr, len(arr), 125), 8)

    def test_recherche_dichotomique(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheDico(arr, 0, len(arr), 100), 7)
        self.assertEqual(TP.rechercheDico(arr, 0, len(arr), 125), 8)

    def test_recherche_trichotomique(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheTrico(arr, 0, len(arr), 100), 7)
        self.assertEqual(TP.rechercheTrico(arr, 0, len(arr), 125), 8)


if __name__ == "__main__":
    nose2.main()
