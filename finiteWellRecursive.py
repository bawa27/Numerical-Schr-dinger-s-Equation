import matplotlib.pyplot as plt
import numpy as np

# Author: Aryan Bawa
# Implements the "Shooting Method" for solving the Time-Independent Schrödinger Equation

BETA = 64
U_STEP = 0.02
EPSILON = 0.0982
PHI_0 = 1.0
RHO_0 = 0

pointlist = []

# Defines a dimensionless square well potential
def square_well_v(u):
    if abs(u) > 1/2:
        return 1
    if abs(u) <= 1/2:
        return 0

# A single step in the numerical integration
def numerical_integration(phi_u, rho_u, u, i):
    pointlist.append((phi_u, u))
    rho_next = rho_u - U_STEP * BETA * (EPSILON - square_well_v(u)) * phi_u
    phi_next = phi_u + U_STEP * rho_u
    if i > 0:
        numerical_integration(phi_next, rho_next, u+U_STEP, i - 1)

def plot_solutions(iterations):
    numerical_integration(PHI_0, RHO_0, 0, iterations)
    y,x = zip(*pointlist)
    plt.scatter(x,y)
    plt.xlabel('u')
    plt.ylabel('phi')
    plt.axhline(0, color='black')
    plt.xlim([0, 2])
    plt.ylim([-1.5, 2])
    plt.show()

# main
plot_solutions(500)