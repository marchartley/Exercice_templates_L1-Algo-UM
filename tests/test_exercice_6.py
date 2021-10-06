import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_6 as TP
import nose2
import unittest

class Test_Exercice6_AlgorithmeDeHeron(unittest.TestCase):
    def test_approximation_de_heron(self):
        self.assertAlmostEqual(TP.approximationHeron(100), 10, places=2)
        self.assertAlmostEqual(TP.approximationHeron(2), 1.4142, places=2)

    def test_version_entiere(self):
        self.assertEqual(TP.approximationHeronPourEntiers(1000), 31)
        self.assertEqual(TP.approximationHeronPourEntiers(16), 4)
        self.assertEqual(TP.approximationHeronPourEntiers(1), 1)


if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 6")
    nose2.main()
