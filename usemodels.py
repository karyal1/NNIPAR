import pickle
from pickle import load
import keras
from keras.models import load_model
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
start = time.process_time()

##For open ocean
model_open = load_model('nniparopen.h5')
inputscalar_open = load(open('inputscaleropen.pkl', 'rb'))
std_open=load(open('outputstdopen.pkl','rb'))

Xopen=np.array([4,0.1,70,0.1,0.2,1,400])## in the order of windspd(m/s),chla(mg/m3),sza(degrees),tau(ext),tau(scat),Angstrom exponent,Ozone(dopsonunit)
Xopen=inputscalar_open.transform([Xopen])
a=model_open.predict([Xopen]).flatten()*std_open

print(a) ##Gives IPAR(0),K_1 and K_2 respectively
  
##For coastal waters
model_coastal = load_model('nniparcoastal.h5')
inputscalar_coastal = load(open('inputscalercoastal.pkl', 'rb'))
std_coastal=load(open('outputstdcoastal.pkl','rb'))

Xcoastal=np.array([4,0.1,70,0.1,0.2,1,400,0.01,0.25,0.075])##in the order of windspd(m/s),chla(mg/m3),sza(degrees),tau(ext),tau(scat),Angstrom exponent,Ozone(dopsonunit),B(660),a(490)(m^-1),b_b(490)(m^-1)
Xcoastal=inputscalar_coastal.transform([Xcoastal])
b=model_coastal.predict([Xcoastal]).flatten()*std_coastal
print(b) ####Gives IPAR(0),K_1 and K_2 respectively

##for vertical profile use predicted a (for oben ocean) or b (for coastal waters)
z=np.arange(0,202,2)
iparz=a[0]*np.exp(-a[1]*z)*np.exp(-a[2]*z/(z+1)**0.5)
print(iparz)

