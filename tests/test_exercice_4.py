import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_4 as TP
import nose2
import unittest

class Test_Exercice4_RechercheDansUneListe(unittest.TestCase):
    def test_recherche_sequentielle(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheSequentielle(arr, len(arr), 100), 7)
        self.assertEqual(TP.rechercheSequentielle(arr, len(arr), 125), 8)

    def test_recherche_dichotomique(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheDicho(arr, 0, len(arr), 100), 7)
        self.assertEqual(TP.rechercheDicho(arr, 0, len(arr), 125), 8)

    def test_recherche_trichotomique(self):
        arr = [0, 2, 8, 16, 32, 33, 33, 100, 125, 455]
        self.assertEqual(TP.rechercheTricho(arr, 0, len(arr), 100), 7)
        self.assertEqual(TP.rechercheTricho(arr, 0, len(arr), 125), 8)


if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 4")
    nose2.main()
