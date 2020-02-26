import matplotlib.pyplot as plt
import cv2
file=open('ex11111111.txt','a+')
#drawfile =open('111111111111111.txt','r')
start_lat=17.829175 #float(input('enter start latitude :'))
end_lat = 17.815669 #float(input('enter end latitude :'))
start_log = 83.337092 #float(input('enter start logitude :'))
end_log = 83.366804 #float(input('enter end logitude :'))
v=int(input('enter velocity :'))
from matplotlib.widgets import Cursor
img = cv2.imread('11.jpg')
xsize = img.shape[1]
ysize =img.shape[0]
latdiff=abs(start_lat-end_lat)
logdiff=abs(start_log-end_log)
#x =[]
#y =[]
"""for i in drawfile:
    i=i.split(',')
    y1=float(i[0])
    x1=float(i[1])
    x.append((ysize*logdiff)*abs(x1-start_log))
    y.append((xsize*latdiff)*abs((y1-start_lat)))"""
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots()
plt.imshow(img1)
#plt.plot(x,y,'*')
cursor = Cursor(ax, horizOn=True, vertOn=True)
def prt():
    fig.canvas.mpl_connect('key_press_event',on)
def on(event):
    try :
        x1 = event.xdata
        y1 = event.ydata
        plt.scatter(x1,y1,c='red',s=5,marker='*')
        print('{0:.6f} , {1:.6f}, {2}\n '.format(start_lat-((y1/ysize)*latdiff),start_log+((x1/xsize)*logdiff),v))
        file.write(f'{start_lat-((y1/ysize)*latdiff):.6f} ,{start_log+((x1/xsize)*logdiff):.6f},{v}\n')
    except:
        pass

def ondraw(event):
    prt()
fig.canvas.mpl_connect('motion_notify_event', ondraw)
plt.show()
cv2.destroyAllWindows()