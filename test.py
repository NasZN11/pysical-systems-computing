# -*- coding: utf-8 -*-

#Import Library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from eulermethod.ode import Ordinary_Differensial_Equation

#Set Range Parameter
dt = 0.01
step = 10000


#Set Initial Values
xs = np.empty(step + 1)
ys = np.empty(step + 1)
zs = np.empty(step + 1)

xs[0], ys[0], zs[0] = (0., 1., 1.05)


ode = Ordinary_Differensial_Equation

#Using Euler Method
for i in range(step):
    x_dot, y_dot, z_dot = ode.lorenz_attractor(xs[i], ys[i], zs[i])
    xs[i+1] = xs[i] +(x_dot * dt)
    ys[i+1] = ys[i] +(y_dot * dt)
    zs[i+1] = zs[i] +(z_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(xs, ys, zs, lw=1)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor (Euler Method)")

plt.show()
