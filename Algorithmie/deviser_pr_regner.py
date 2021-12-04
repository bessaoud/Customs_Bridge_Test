import random


# Implémentation de l'algorithme de "Diviser Pour Mieux Régner"
def DPMR(L, min_i, max_i, element):
    """
    Description
    ----------
    DPMR: Cette fonction permet de trouver la bonne position\\
          en terme d'ordre croissant dans laquelle un élément\\
          sera inseré dans une liste triée.
    Parameters
    ----------
    L : Une liste d'élèments ayant un ordre croissant.
    min_i: L'indice minimal de la liste L.
    max_i: L'indice maximal de la liste L.
    élément : une nouvelle valeur à insérer dans L.
    """
    mid = (min_i + max_i)//2
    if (min_i == max_i) or (min_i == max_i-1):
        if (element <= L[mid]):
            return mid
        else:
            return mid+1
    else:
        if (element > L[mid]):
            return DPMR(L, mid, max_i, element)
        else:
            return DPMR(L, min_i, mid, element)


# Programme
try:
  LONGUEUR = int(input("Saisis la longueur de la liste: "))
  MIN = int(input("Saisis la valeur minimale: "))
  MAX = int(input("Saisis la valeur maximale: "))
except ValueError:
  print('Erreur: la longueur de la liste L, le Min et le Max doivent être des entiers')
if MAX < MIN: 
   print('Erreur: la valeur maximal doit être plus grande que celle minimale')
else:
    if MAX >= LONGUEUR:
        # random.sample: génére aléatoirement 'LONGUEUR' éléments\\
        # entiers sans répétition entre MIN et MAX-1.
        L = random.sample(range(MIN, MAX+1), LONGUEUR)
    else:
        # random.randint: retourne aléatoirement un élément entre\\
        # MIN et MAX. On poura avoir des répétitions dans ce cas là.
        L = [random.randint(MIN, MAX) for i in range(LONGUEUR)]
    L = sorted(L)
    element = random.randint(MIN, MAX)
    print("le nouveau élément généré est: ", element)
    element_i = DPMR(L, 0, LONGUEUR-1, element)
    print("la position de l'élément généré est: ", element_i)
    L_final = L[:element_i] + [element] + L[element_i:]
    print("L'ancienne liste: ", L)
    print("La nouvelle liste: ", L_final)
