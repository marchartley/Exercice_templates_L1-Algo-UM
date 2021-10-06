import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_1 as TP
import nose2
import unittest

class Test_Exercice1_Binomes(unittest.TestCase):
    def test_calcul_binomial(self):
        self.assertEqual(TP.binome(5, 2), 10)
        self.assertEqual(TP.binome(10, 5), 252)

    def test_calcul_binomial_efficace(self):
        self.assertEqual(TP.binomeEfficace(5, 2), 10)
        self.assertEqual(TP.binomeEfficace(10, 5), 252)

if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 1...")
    nose2.main()
