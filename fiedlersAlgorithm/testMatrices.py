import numpy as np

# Chain from A-D
#                A  B  C  D
a = np.array([  [0, 1, 0, 0],#  A
                [1, 0, 1, 0],#  B
                [0, 1, 0, 1],#  C
                [0, 0, 1, 0]])# D 
    

# Two groups of 3 combined at a single link (A, B, C) <-> (D, E, F)
#                A  B  C  D  E  F
b = np.array([  [0, 1, 1, 0, 0, 0],  # A
                [1, 0, 1, 0, 0, 0],  # B
                [1, 1, 0, 1, 0, 0],  # C
                [0, 0, 1, 0, 1, 1],  # D
                [0, 0, 0, 1, 0, 1],  # E
                [0, 0, 0, 1, 1, 0]]) # F


# (Group of 3 <--> Group of 4) intermixed
# Example 12.1 Revisited from Graph Theory - Justin Wyss-Gallifent
#                A  B  C  D  E  F  G
c = np.array([  [0, 0, 1, 0, 0, 1, 0],  # A
                [0, 0, 1, 1, 1, 0, 0],  # B
                [1, 1, 0, 0, 0, 1, 0],  # C
                [0, 1, 0, 0, 0, 0, 1],  # D
                [0, 1, 0, 0, 0, 0, 1],  # E
                [1, 0, 1, 0, 0, 0, 0],  # F
                [0, 0, 0, 1, 1, 0, 0]]) # G



# Two mixed up groups of 4 connected by 1-2 edges
#                A  B  C  D  E  F  G  H
d = np.array([  [0, 1, 0, 1, 0, 0, 0, 0], # A
                [1, 0, 1, 0, 0, 0, 0, 0], # B
                [0, 1, 0, 1, 0, 0, 0, 0], # C
                [1, 0, 1, 0, 1, 0, 0, 0], # D
                [0, 0, 0, 1, 0, 1, 0, 1], # E
                [0, 0, 0, 0, 1, 0, 1, 0], # F
                [0, 0, 0, 0, 0, 1, 0, 1], # G
                [0, 0, 0, 0, 1, 0, 1, 0]])# H
