""" Module Utile

Module pour les fonctions utiles

 - sous-fonctions pour le tri, ...

"""

import numpy as np

def generate_Y(n,m):

    s=m/4

    return np.random.normal(m,s,(n,2))

def dominate(a,b):

    if a[0] < b[0] and a[1] < b[1]:
        return True
    else :
        return False

"""
Partie Tri Fusion
"""


def is_ordre_lexico(a, b):
    # Implementation pour une liste de 2 éléments
    if a[0] < b[0] or a[0] == b[0] and a[1] < b[1]:
        return True
    else:
        return False


def fusion(A, B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif is_ordre_lexico(A[0], B[0]):
        return np.concatenate(([A[0]], fusion(A[1:], B)), axis=0)
    else:
        return np.concatenate(([B[0]], fusion(A, B[1:])), axis=0)


def tri_fusion(T):  # Implementation maison
    # https://fr.wikipedia.org/wiki/Tri_fusion
    n = len(T)
    if n <= 1:
        return T
    else:
        return fusion(tri_fusion(T[: n // 2]), tri_fusion(T[(n // 2) :]))


def tri_sys(T):  # Alternative
    # https://numpy.org/devdocs/reference/generated/numpy.lexsort.html
    return np.array([T[i] for i in np.lexsort((T[:, 1], T[:, 0]))])
