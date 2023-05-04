import numpy as np
import matplotlib.pyplot as plt

filepath_U1 = r"C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\U1_matrix.txt"
filepath_U2 = r"C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\U2_matrix.txt"
filepath_x = r"C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\Vector_x.txt"
filepath_t = r"C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\Vector_t.txt"
U1 = np.loadtxt(filepath_U1, dtype=float)
U2 = np.loadtxt(filepath_U2, dtype=float)
x = np.loadtxt(filepath_x, dtype=float)
t = np.loadtxt(filepath_t, dtype=float)
#явная 3д
xgrid, tgrid = np.meshgrid(x, t)
fig1 = plt.figure()
ax = fig1.add_subplot(projection='3d')
ax.plot_surface(np.array(xgrid), np.array(tgrid), np.array(U1), cmap='viridis')
ax.set_title('Явная схема, C++')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('U')
plt.show()
#неявная 3д
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
ax2.plot_surface(np.array(xgrid),np.array(tgrid),np.array(U2),cmap='viridis')
ax2.set_title('Неявная схема, C++')
ax2.set_xlabel('x')
ax2.set_ylabel('t')
ax2.set_zlabel('U')
plt.show()

fig1.savefig(r'C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\U1.png', dpi=300, bbox_inches='tight')
fig1.savefig(r'C:\Users\Harry Potter\Desktop\Project\ProjectPluses\ProjectPluses\U2.png', dpi=300, bbox_inches='tight')