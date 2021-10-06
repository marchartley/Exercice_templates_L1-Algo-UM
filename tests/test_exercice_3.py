import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exercice_3 as TP
import nose2
import unittest
import io
from contextlib import redirect_stdout

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

if __name__ == "__main__":
    print("Lancement de la verification de l'exercice 3")
    nose2.main()
