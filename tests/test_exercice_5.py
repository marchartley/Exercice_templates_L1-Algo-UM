import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_5 as TP
import nose2
import unittest

class Test_Exercice5_CalculSousSuiteDeSommeMax(unittest.TestCase):
    def test_algorithme_naif(self):
        arr = [1, 2, 1]
        self.assertEqual(TP.maxSumNaif(arr), 4)
        arr = [100, -1, 3, 5, -50, 10, 10, 5]
        self.assertEqual(TP.maxSumNaif(arr), 107)

    def test_algorithme_avec_formule(self):
        arr = [-5, 10, 10, -2, 3]
        self.assertEqual(TP.maxSumAvecEquation(arr), 21)
        arr = [1, -8, 3, 10, -4, 10]
        self.assertEqual(TP.maxSumAvecEquation(arr), 19)

    def test_diviser_pour_regner(self):
        arr = [7, 2, -4, 2, 7]
        self.assertEqual(TP.maxSumDiviserPourRegner(arr), 14)
        arr = [-2, 1, 10, -4, 2, -5]
        self.assertEqual(TP.maxSumDiviserPourRegner(arr), 11)


if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 5")
    nose2.main()
