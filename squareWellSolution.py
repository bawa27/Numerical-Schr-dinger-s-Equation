import matplotlib.pyplot as plt

# Author: Aryan Bawa
# Dedicated to Kendall Yoon (she made me put this here)
# Implements the "Shooting Method" for solving the Time-Independent Schrödinger Equation

BETA = 64
U_STEP = 0.05
X_LIM = [0,2]
Y_LIM = [-1.5,1.5]

# Defines a dimensionless square well potential
def square_well_v(u):
    if abs(u) > 1/2:
        return 1
    if abs(u) <= 1/2:
        return 0

# A single step in the numerical integration using Eq. (8) and (9) in the handout
def numerical_step(phi_u, rho_u, u, epsilon):
    rho_next = rho_u - U_STEP * BETA * (epsilon - square_well_v(u)) * phi_u
    phi_next = phi_u + U_STEP * rho_u
    return phi_next, rho_next

# determines the phi value of each point by iterating over each numerical integration step
def numerical_integration(phi_0, rho_0, epsilon, iterations):
    pointlist = [(0, phi_0)]
    phi = phi_0
    rho = rho_0

    # iterations are just defined by how many points you want to show up
    for i in range(iterations):
        # range starts at 0, so we use i+1 here
        u = U_STEP * (i+1)
        phi, rho = (numerical_step(phi, rho, u, epsilon))
        point = (u, phi)
        pointlist.append(point)

    return pointlist

# uses matplotlib to plot the solutions
def plot_solutions(phi_0, rho_0, epsilon, number_of_points):
    # extract x,y values from point and store them in their own lists
    x,y = zip(*numerical_integration(phi_0, rho_0, epsilon, number_of_points))

    # storing everything in a figure
    figure = plt.figure()

    # creating a scatter plot with x,y lists, adding labels, setting graph limits, etc.
    plt.scatter(x,y, s = 10)
    plt.xlabel('u')
    plt.ylabel('φ(u)')
    plt.axhline(0, color='black', linestyle='--')
    plt.ylim(Y_LIM)
    plt.xlim(X_LIM)
    plt.title("ε = " + str(epsilon))

    # returning the figure
    return figure

# main
# searching for solutions by testing different epsilon values
plot_solutions(1.0, 0, 0.1, 50).show()

# the above value had negative curvature, so let's turn down the value of epsilon until the
# curvature switches back around
plot_solutions(1.0, 0, 0.09, 50).show()
plot_solutions(1.0, 0, 0.095, 50).show()
plot_solutions(1.0, 0, 0.097, 50).show()
plot_solutions(1.0, 0, 0.098, 50).show()
plot_solutions(1.0, 0, 0.099, 50).show()

# okay, we had a switch. let's go one digit further into the previous epsilon value and
# evaluate further
plot_solutions(1.0, 0, 0.0985, 50).show()
plot_solutions(1.0, 0, 0.0987, 50).show()
plot_solutions(1.0, 0, 0.0988, 50).show()

# As 0.0987 was the final 4 digit value without negative curvature, we find that
# epsilon = 0.0987 up to the fourth digit

# extract x,y values from point and store them in their own lists
x,y = zip(*numerical_integration(1.0, 0, 0.0987, 50))
xa,ya = zip(*numerical_integration(1.0, 0, 0.098, 50))
xb,yb = zip(*numerical_integration(1.0, 0, 0.099, 50))

# storing everything in a figure
figure = plt.figure()
ax1 = figure.add_subplot(111)

# creating a scatter plot with x,y lists, adding labels, setting graph limits, etc.
ax1.scatter(x,y, s = 10, color='purple', label = "ε = 0.0987")
ax1.scatter(xa,ya, s = 10, color='blue', label = "ε = 0.098")
ax1.scatter(xb,yb, s = 10, color='red', label = "ε = 0.099")


plt.xlabel('u')
plt.ylabel('φ(u)')
plt.axhline(0, color='black', linestyle='--')
plt.ylim(Y_LIM)
plt.xlim(X_LIM)
plt.title("Numerical Solution of the Finite Well Schrödinger Equation")

figure.legend(bbox_to_anchor=(0.2, 0.2), loc = "lower left")
figure.show()

# saving the figure (uncomment to save)
# figure.savefig("finite_well_solution.pdf", format = "pdf")