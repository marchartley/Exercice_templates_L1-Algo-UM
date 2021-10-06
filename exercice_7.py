# Exercice 7:

# L'algorithme en Python est donné ici.
# Considerez le nombre binaire écrit dans le sens inverse:
# ex: le nombre binaire 110 (= 6 en décimal) est traduit en un
#     tableau a = [0, 1, 1]
def incrementation(a):
    i = 0
    n = len(a)
    while i < n and a[i] == 1:
        a[i] = 0
        i += 1
    if i < n:
        a[i] = 1

    # Petit ajout pour ne pas tronquer la valeurs finale:
    # Si on a incrémenté le dernier bit, on ajoute un "1" à la fin du tableau
    if i == n:
        a.append(1)
    return a

def analyseDeLalgorithme():
    print("""
    L'algorithme est valide.
    Il se termine car ...
    Le resultat est correct car ...

    La complexite en temps est ...
    La complexite en memoire est ...
    En moyenne, la complexite en temps est ...
    """)
