import pickle
from tensorflow.keras.models import load_model
import sklearn
import h5py
import numpy as np
import matplotlib.pyplot as plt
import time
start = time.process_time()
from IPython.display import display, Math
import warnings

def load(x):
    with warnings.catch_warnings():
          warnings.simplefilter("ignore", category=UserWarning)
          return pickle.load(open(x,'rb'))

def nnopen(wind,chla,sza,tau,omega,alpha,ozone):
    model_open = load_model('s1nniparopen.h5',compile=None)
    inputscalar_open = load('sinputscalaropen.pkl')
    outputscalar_open=load('soutputstdopen.pkl')
    Xopen=np.array([wind,chla,sza,tau,omega,alpha,ozone])
    Xopen=inputscalar_open.transform([Xopen])
    a=outputscalar_open.inverse_transform(model_open.predict([Xopen])).flatten()
    return a
    
    
def nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb):
    model_coastal = load_model('s1tnniparcoastal.h5',compile = False)
    inputscalar_coastal = load('s1tinputscalarcoastal.pkl')
    outputscalar_coastal=load('s1toutputstdcoastal.pkl')
    Xcoastal=np.array([wind,chla,sza,tau,omega,alpha,ozone,B,a,bb])
    Xcoastal=inputscalar_coastal.transform([Xcoastal])
    a=model_coastal.predict([Xcoastal])
    a=outputscalar_coastal.inverse_transform(model_coastal.predict([Xcoastal])).flatten()
    return a
    
def verticalprofile(x):
    a=x
    z=np.arange(0,202,2)
    iparz=a[0]*np.exp(-a[1]*z)*np.exp(-a[2]*z/(z+1)**0.5)
    print(iparz)
    return iparz
    
##Users can adjust the value of different input parameters within the given range
##The parameters B, a, and bb are used only for coastal waters NN model.
## Function nnopen() and nncoastal() give an array of IPAR(0^-),K_1,K_2 for corresponding cases
## function verticalprofile(x) takes output from NN model as input and can be used to get IPAR vertical profile for corresponding case

wind=4          ##wind speed (m/s), range=(0.5-10)
chla=0.1        ##chla(mg/m3), range=(0.001,30)
sza=74          ##sza(degrees), range=(0,82)
tau=0.4         ##Extinction Aerosol optical depth, range=(0,0.5)
omega=0.9       ##single scattering albedo, range=(0.88,0.99)
alpha=1         ##angstrom exponent, range=(-0.06,1.45)
ozone=400       ##Ozone column (dobson unit), range=(150,450)
B=0.05          ##Backscattering fraction at 670 nm (unitless), range=(0.002,0.05)
a=0.25          ##absorption coefficient at 490 nm (m-1), range=(0.015-1.274)
bb=0.075        ##backscattering coefficient at 490 nm(m_1), range=(0.001-0.116)
print(nnopen(wind,chla,sza,tau,omega,alpha,ozone)) ##prints an array of (IPAR(0^-),K_1 and K_2) for open ocean
verticalprofile(nnopen(wind,chla,sza,tau,omega,alpha,ozone))## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for open waters
    

print(nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb)) ####prints an array of (IPAR(0^-),K_1 and K_2) for coastal waters
verticalprofile(nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb)) ## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for coastal waters
    