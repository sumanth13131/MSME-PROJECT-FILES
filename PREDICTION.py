import joblib
import  numpy as np
lat=float(input('enter latitude :-'))
log=float(input('enter logitude :-'))

loaded_model = joblib.load(open('models.sav', 'rb'))
b=[[lat],[log]]
a=np.array(b)
c=np.transpose(a)
try :
    speed = loaded_model.predict(c)
    print(speed[0])
except:
    pass