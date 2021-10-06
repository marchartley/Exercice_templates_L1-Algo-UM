# Exercice 6:
from math import sqrt
# 1. Montrer que la suite (x_n) est décroissante à partir du rang 1 et
#    qu’elle converge effectivement vers sqrt(a).
#    L’algorithme de Heron mérite-t-il vraiment l’appellation d’algorithme ?
def demonstrationHeron():
    print("""
    La suite (x_n) est décroissante à partir du rang 1 car ...

    Elle converge vers sqrt(a) car ...

    On peut le considerer comme un algorithme car ...
    On ne peut pas le considerer comme un algorithme car ...
    """)

# Implémenter la fonction qui calcule la suite (x_n)
# Vous pouvez laisser une valeur x_0 par défaut supérieure à 0
# Arrêtez la fonction lorsque la différence entre x et sqrt(a) est inférieure
# à 0.01 (vous pouvez utiliser la fonction sqrt uniquement pour la condition)
# Hint: utilisez "if abs( x - sqrt(a) ) < 0.01"
def approximationHeron(a, x = 1):
    x = (x + a/x)/2
    if abs(x - sqrt(a)) < 0.01:
        return x
    else:
        return approximationHeron(a, x)
    pass

# 2. On suppose maintenant que a est entier et l’on souhaite calculer la racine
#    carrée entière de a c’est-à-dire l’entier naturel b
#    tel que b2 <= a < (b + 1)2. Plutôt que d’appliquer "l’algorithme" de Heron,
#    on lui substitue une version entière :
#    Choisir x0 entier strictement positif et calculer x1; ... ; xn; ... par
#    la relation x_(k+1) = int( (x_k + a/x_k) /2 ) où int( x ) désigne
#    la partie entière de x. Arrêter les calculs dès que l’on obtient deux
#    valeurs successives xn et x_(n+1) telles que x_n <= x_(n+1) et n > 0.
#    Retourner x_n.
def approximationHeronPourEntiers(a, x = 1):
    pass

#    Démonter que cet algorithme est valide (c’est-à-dire qu’il termine et
#    fournit le résultat correct).
def demonstrationHeronPourEntiers():
    print("""
    L'algorithme de Heron version entiere est valide.
    En effet elle termine car ...

    De plus le resultat est correct car ...
    """)
