#-------- PROBLEMA TRANSPORT
import numpy as np
from funcions import Vogel
# Introduir matriu de costes , Ofertes y Demand3s
Mab=np.array([
    [80,  50, 60],
    [7, 100, 90],
    [40, 30, 20]
    ])

ac=np.array([80, 70, 65])

bc=np.array([65, 30, 70])

# Torna la matriu otiginal amb les modificacions (ficticis)
# també torna els repartiments (pas a pas)
Mab0, Mc= Vogel(Mab,ac,bc)

sum(sum(Mab0*Mc))


