import pickle
from pickle import load
import keras
from keras.models import load_model
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
start = time.process_time()
from IPython.display import display, Math


def nnopen(wind,chla,sza,tau,omega,alpha,ozone):
    model_open = load_model('s1nniparopen.h5')
    inputscalar_open = load(open('sinputscalaropen.pkl', 'rb'))
    outputscalar_open=load(open('soutputstdopen.pkl','rb'))
    Xopen=np.array([wind,chla,sza,tau,omega,alpha,ozone])
    Xopen=inputscalar_open.transform([Xopen])
    a=outputscalar_open.inverse_transform(model_open.predict([Xopen]).flatten())
    print (a)
    return a
    
    
def nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb):
    model_coastal = load_model('s1tnniparcoastal.h5')
    inputscalar_coastal = load(open('s1tinputscalarcoastal.pkl', 'rb'))
    outputscalar_coastal=load(open('s1toutputstdcoastal.pkl','rb'))
    Xcoastal=np.array([wind,chla,sza,tau,omega,alpha,ozone,B,a,bb])
    Xcoastal=inputscalar_coastal.transform([Xcoastal])
    a=outputscalar_coastal.inverse_transform(model_coastal.predict([Xcoastal]).flatten())
    print (a)
    return a
    
def verticalprofile(x):
    a=x
    z=np.arange(0,202,2)
    iparz=a[0]*np.exp(-a[1]*z)*np.exp(-a[2]*z/(z+1)**0.5)
    print(iparz)
    return iparz
    
    

wind=4          ##wind speed in m/s
chla=0.1        ##chla(mg/m3)
sza=74          ##sza(degrees)
tau=0.4         ##Extinction Aerosol optical depth
omega=0.9       ##single scattering albedo
alpha=1         ##angstrom exponent
ozone=400       ##Ozone column in dobson unit
B=0.05          ##Backscattering fraction
a=0.25          ##absorption coefficient (m-1)
bb=0.075        ##backscattering coefficient(m_1)
nnopen(wind,chla,sza,tau,omega,alpha,ozone) ##prints an array of (IPAR(0^-),K_1 and K_2) for open ocean
verticalprofile(nnopen(wind,chla,sza,tau,omega,alpha,ozone))## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for open waters
    

nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb) ####prints an array of (IPAR(0^-),K_1 and K_2) for coastal waters
verticalprofile(nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb)) ## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for coastal waters
    