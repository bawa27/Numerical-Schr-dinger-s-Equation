import matplotlib.pyplot as plt
import numpy as np

# Author: Aryan Bawa
# Implements the "Shooting Method" for solving the Time-Independent Schrödinger Equation

BETA = 64
U_STEP = 0.5
EPSILON = 0.1
PHI_0 = 1.0
RHO_0 = 0

# Defines a dimensionless square well potential
def square_well_v(u):
    if abs(u) > 1/2:
        return 1
    if abs(u) <= 1/2:
        return 0

# A single step in the numerical integration
def numerical_step(phi_u, rho_u, u):
    rho_next = rho_u - U_STEP * BETA * (EPSILON - square_well_v(u)) * phi_u
    phi_next = phi_u + U_STEP * rho_u
    return u, phi_next

def numerical_integration(iterations):
    pointlist = [(0, PHI_0)]
    for i in range(iterations):
        point = (numerical_step(PHI_0, RHO_0, U_STEP * (i + 1)))
        pointlist.append(point)
    return pointlist

def plot_solutions(iterations):
    x,y = zip(*numerical_integration(iterations))
    plt.scatter(x,y)
    plt.xlabel('u')
    plt.ylabel('phi')
    # plt.xlim([-100, 100])
    # plt.ylim([-100, 100])
    plt.show()

# main
plot_solutions(100)


