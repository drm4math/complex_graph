import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as mp3d
from matplotlib.widgets import Slider


scale = 4
weight = 2

def draw_axis_3D(ax):
    xaxis_line_x = np.linspace(-scale, scale, 1000)
    xaxis_line_y = np.zeros(xaxis_line_x.shape)
    xaxis_line_z = np.zeros(xaxis_line_x.shape)
    ax.plot3D(xaxis_line_x, xaxis_line_y, xaxis_line_z, 'gray')

    yaxis_line_y = np.linspace(-scale, scale, 1000)
    yaxis_line_x = np.zeros(yaxis_line_y.shape)
    yaxis_line_z = np.zeros(yaxis_line_y.shape)
    ax.plot3D(yaxis_line_x, yaxis_line_y, yaxis_line_z, 'gray')

    zaxis_line_z = np.linspace(-scale, scale, 1000)
    zaxis_line_y = np.zeros(zaxis_line_z.shape)
    zaxis_line_x = np.zeros(zaxis_line_z.shape)
    ax.plot3D(zaxis_line_x, zaxis_line_y, zaxis_line_z, 'gray')


def draw_axis_plane(ax):
    a = np.array([( 0, 0, 0),( scale, 0, 0),( scale, scale, 0),( 0, scale, 0)])
    R1 = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    R2 = (R1[::-1].T)[:,[1,0,2]]
    R3 = (R1[::-1])[:,[1,0,2]]
    f = lambda a,r: np.matmul(r, a.T).T
    g = lambda a,r: [a, f(a,r), f(f(a,r),r), f(f(f(a,r),r),r)]

    for i, ind , r in zip(range(3),[[0,1,2],[2,0,1],[1,2,0]], [R1,R2,R3]):
        xy = g(a[:,ind], r )
        for x in xy:
            face1 = mp3d.art3d.Poly3DCollection([x] , alpha=0.1, linewidth=1)
            face1.set_facecolor((i//2, i%2, i==0,  0.5))
            ax.add_collection3d(face1)



x0 = scale
x_step = 0.1

a0 = 310
a_step = 1

x_line = np.linspace(-scale, x0, 1000)
y_line = np.cos(np.pi*x_line) * np.power(weight, x_line)
z_line = np.sin(np.pi*x_line) * np.power(weight, x_line)

xpts = np.arange(-scale,x0+0.1, 1)
ypts = np.cos(np.pi*xpts) * np.power(weight, xpts)
zpts = np.sin(np.pi*xpts) * np.power(weight, xpts)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
fig.subplots_adjust(bottom=0.35)
# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.35)
# ax.axes(projection="3d")

ax.set_xlabel('x')
ax.set_ylabel('Re_y')
ax.set_zlabel('Im_y')
ax.set_xlim3d(-scale,scale)
ax.set_ylim3d(-scale,scale)
ax.set_zlim3d(-scale,scale)
ax.view_init(30, a0)

draw_axis_3D(ax)
draw_axis_plane(ax)
l = ax.plot3D(x_line, y_line, z_line, 'blue')
p = ax.scatter3D(xpts, ypts, zpts, c='black')

axcolor = 'lightgoldenrodyellow'
ax_x = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_z = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sld_x = Slider(ax_x, 'x val', -scale, scale, valinit=x0, valfmt='%.1f', valstep=x_step)
sld_z = Slider(ax_z, 'Im_y view', 0, 360, valinit=a0, valfmt='%d', valstep=a_step)


def update(val):
    xi = sld_x.val
    ai = sld_z.val

    x_line = np.linspace(-scale, xi, 1000)
    y_line = np.cos(np.pi*x_line) * np.power(weight, x_line)
    z_line = np.sin(np.pi*x_line) * np.power(weight, x_line)
    
    xpts = np.arange(-scale,xi+0.1, 1)
    ypts = np.cos(np.pi*xpts) * np.power(weight, xpts)
    zpts = np.sin(np.pi*xpts) * np.power(weight, xpts)
    elev = ax.elev

    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('Re_y')
    ax.set_zlabel('Im_y')
    ax.set_xlim3d(-scale,scale)
    ax.set_ylim3d(-scale,scale)
    ax.set_zlim3d(-scale,scale)
    ax.view_init(azim=ai)

    draw_axis_3D(ax)
    draw_axis_plane(ax)
    l = ax.plot3D(x_line, y_line, z_line, 'blue')
    p = ax.scatter3D(xpts, ypts, zpts, c='black')


    # l[0].set_data_3d(x_line, y_line, z_line)
    # fig.canvas.draw_idle()

    ax.view_init(elev, ai)


sld_x.on_changed(update)
sld_z.on_changed(update)

plt.show()




# def main():
#     fig = plt.figure()
#     ax = plt.axes(projection="3d")

    
    

    


    


#     # z_points = 15 * np.random.random(100)
#     # x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
#     # y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
#     # ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')

#     plt.show()



# if __name__ == '__main__':
#     main()