import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    return x, y, z

x, y, z = load_data('C:/Users/asus/Desktop/New Text Document.csv')

# Calculate and plot histograms of x, y, and z
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
ax1.hist(x, bins=50)
ax1.set_title('X')
ax2.hist(y, bins=50)
ax2.set_title('Y')
ax3.hist(z, bins=50)
ax3.set_title('Z')
plt.show()

# Plot the data points as a 3D scatter plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
