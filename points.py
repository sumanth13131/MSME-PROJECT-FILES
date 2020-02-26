import matplotlib.pyplot as plt
import cv2
file=open('ex5.txt','a+')
left=float(input('enter left logitude'))
right = float(input('enter right logitude'))
top = float(input('enter top latitude'))
bottom = float(input('enter bottom latitude'))
v=int(input())
from matplotlib.widgets import Cursor
img = cv2.imread('1.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots()
#plt.xlim([left,right])
#plt.ylim([top ,bottom])
plt.imshow(img1)
cursor = Cursor(ax, horizOn=True, vertOn=True)
def prt():
    fig.canvas.mpl_connect('key_press_event',on)
def on(event):
    try :
        x1 = event.xdata + left
        y1 = event.ydata + bottom
        #print(type(x1))
        print('{0:.6f} , {1:.6f}, {2}\n '.format(x1, y1,v))
        file.write(f'{x1:.6f} , {y1:.6f},{v}\n')
    except:
        pass

def ondraw(event):
    prt()
fig.canvas.mpl_connect('motion_notify_event', ondraw)
plt.show()
cv2.destroyAllWindows()