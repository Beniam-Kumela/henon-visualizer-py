#Import modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from tqdm import tqdm

#User dialogue
print('''
Welcome to the Hénon Map Animator!
We will animate the formation of the Hénon attractor.
This is a well-studied dynamical system which is known to exhibit chaotic behavior.
Let's get started by specifying by initializing conditions.
''')

color = input("Enter first letter of color here (k for black): ")
print("Now specify how many iterations you want calculated for each point.")
n_iter = int(input("Enter iterations here (more = better resolution): "))
print("Finally, how many frames do you want the animation to be?")
F = int(input("Enter frames here (>140): "))

# Initialize remaning conditions
x = 0.01
y = 0.01
x_val = []
y_val = []
fig, ax = plt.subplots()

#Define Henon Map function
def Henon_Map(x, y, a, b=0.3):
    
    xnew = 1 - a * x ** 2 + y
    ynew = b * x
    
    return xnew, ynew

#Create animation function and plot collected data
def animate(frame):
    global x, y
    
    a = frame * 0.01
    x_val.clear()
    y_val.clear()
    ax.clear()
    for i in range(n_iter):
        x, y = Henon_Map(x, y, a)
        x_val.append(x)
        y_val.append(y)
    
    ax.scatter(x_val, y_val, c = color, s = 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-1, 1])
    ax.set_title('Henon Map for a = ' + str(round(a,2)) + ' and b = 0.3 for ' + str(n_iter) + ' iterations each')

#Save animation as a video
anim = FuncAnimation(fig, animate, frames = tqdm(range(F), initial=1, position=0), interval = 200, repeat = True)
anim.save('Henon Map Evolution.gif', writer = 'Pillow')

print("Animation was succesfully made and saved as 'Henon Map Evolution.gif' within the 'dist' folder.")
time.sleep(5)
plt.close()