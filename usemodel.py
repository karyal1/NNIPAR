from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pickle
from pickle import dump
from pickle import load
from tensorflow import keras as keras
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import h5py
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
#from tensorflow import keras as keras
from keras.layers import LeakyReLU
#from numpy import loadtxt
from keras import callbacks
from keras.models import Sequential
from keras.layers import Dense
#from sklearn.preprocessing import StandardScaler
#from sklearn.preprocessing import MinMaxScaler
import h5py
import matplotlib.pyplot as plt
#from keras.optimizers import SGD
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import r2_score
from keras.callbacks import LearningRateScheduler
from keras.regularizers import l2
#import tensorflow_addons as tfa



#modelo=load_model('euipar11.h5')
#modelc=load_model('ceuipar218.h5')
#modelc=load_model('dolptrainadamwgragain4lui.h5')
model = load_model('nniparopen.h5')
#model=load_model(model)
# load the scaler
inputscaler = load(open('inputscaleropen.pkl', 'rb'))
std1=load(open('outputstdopen.pkl','rb'))
print(inputscaler)
print(std1)
f=h5py.File('dblopenneuralinput.h5','r')
dataset=f['arr2'][:]
#f1=h5py.File('li_data_1.h5','r')
#litest=f1['arr2'][:]
#dataset[:,1]=np.cos(1/180*np.pi*dataset[:,1])
#litest[:,0]=1/30*litest[:,0]
#litest1=litest[:,0:6:1]
#m1=max(dataset[:,16])
#dataset[:,0]=1/30*dataset[:,0]
#dataset[:,2]=np.cos(1/180*np.pi*dataset[:,2])
#dataset[:,16]=dataset[:,16]/m1
#print(dataset.shape)
X=dataset[:,:]
Y = dataset[:,16:]

Xtrval1, Xtest1, Ytrval, Ytest = train_test_split(X, Y, test_size=0.1317, random_state=1)
Xtrain1, Xval1, Ytrain, Yval = train_test_split(Xtrval1, Ytrval, test_size=0.1, random_state=1)
#print(Xtrain.shape)

#print(Xval.shape)
#dataset1=Ytest
Xtest=Xtest1[:,0:7]
Xval=Xval1[:,0:7]
Xtrain=Xtrain1[:,0:7]
Ytrain1=Ytrain[:,0:3:1]
#std1=Ytrain1.std()
Yval1=Yval[:,0:3:1]
Ytest1=Ytest[:,0:3:1]
Xtest=inputscaler.transform(Xtest)
a3=[]
a4=[]

#for i in range (Xtrain.shape[0]):
for i in range (Xtest.shape[0]):
#for i in range(0,200):
   a1=[]
#   a=model1.predict(np.array([Xtrain[i,0:5:1]]))
   a=model.predict(np.array([Xtest[i,0:7:1]]))
   b=a.flatten()
   x=b[0]*std1[0]
   y=b[1]*std1[1]
   y1=b[2]*std1[2]
#   c1=dataset1[i,7]
#   c2=Ytrain[i]*m1
#   c2=Ytest1[i,0]*m1
#   d2=Ytest1[i,1]
#   d21=Ytest1[i,2]
#   print(x,dataset[i,7])
#   print(y,dataset[i,8])
#   a1=x
#   a2=x*m1
#   b2=y


   a1.append(x)
   a1.append(y)
   a1.append(y1)
#   a1.append(b2)
#   a1.append(d21)
#   a1.append(y1)
   a3.append(a1)
a3=np.array(a3)
dataset2=np.concatenate((Xtest1,a3),axis=1)
with h5py.File('nniparopenpk.h5', 'w') as hf:
    hf.create_dataset("arr2",  data=dataset2)

#model.fit(X, Y, epochs=8000, batch_size=40, callbacks=[callbacks])

