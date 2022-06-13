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
    a=outputscalar_open.inverse_transform(model_open([Xopen])).flatten()
    return a
    
    
def nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb):
    model_coastal = load_model('s1tnniparcoastal.h5',compile = False)
    inputscalar_coastal = load('s1tinputscalarcoastal.pkl')
    outputscalar_coastal=load('s1toutputstdcoastal.pkl')
    Xcoastal=np.array([wind,chla,sza,tau,omega,alpha,ozone,B,a,bb])
    Xcoastal=inputscalar_coastal.transform([Xcoastal])
    a=outputscalar_coastal.inverse_transform(model_coastal([Xcoastal])).flatten()
    return a
    
def verticalprofile(x):
    a=x
    z=np.arange(0,202,2)
    iparz=a[0]*np.exp(-a[1]*z)*np.exp(-a[2]*z/(z+1)**0.5)
    print(iparz)
    return iparz
    
# Test cases for open ocean and coastal waters to check performance of package in users' environment
#model and enviroment are up to date when the predicted values match with reference predictions 
testopen=[[4,0.1,74,0.4,0.9,1,400],[8,2,30,0.3,0.95,1.3,350],[2,10,55,0.1,0.97,0.5,380]]
testcoastal=[[4,0.1,74,0.4,0.9,1,400,0.05,0.25,0.075],[8,2,30,0.3,0.95,1.3,350,0.01,1.1,0.1],[2,10,55,0.1,0.97,0.5,380,0.03,0.6,0.5]]

print(nnopen(*testopen[0]),nnopen(*testopen[1]),nnopen(*testopen[2]))
print('Reference predictions: [1.3082751e+02 4.0552534e-02 3.9834082e-01] [1.3257466e+03 2.4190046e-01 2.0054483e-01] [1.0634016e+03 4.9300832e-01 3.7214747e-01]  ')
print(nncoastal(*testcoastal[0]),nncoastal(*testcoastal[1]),nncoastal(*testcoastal[2]))
print('Reference predictions: [ 1.4436867e+02 -4.0723542e-03  1.7823621e+00] [1.3895797e+03 2.4155480e-01 2.3116295e+00] [8.3044104e+02 7.6482791e-01 3.2773843e+00]')

##Users can adjust the value of different input parameters within the given range as needed.
##The parameters B, a, and bb are used only for coastal waters NN model.
## Function nnopen() and nncoastal() give an array of IPAR(0^-),K_1,K_2 for corresponding cases
## function verticalprofile(x) takes output from NN model's output as input and can be used to get IPAR vertical profile for corresponding case

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
# verticalprofile(nnopen(wind,chla,sza,tau,omega,alpha,ozone))## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for open waters
    

print(nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb)) ####prints an array of (IPAR(0^-),K_1 and K_2) for coastal waters
# verticalprofile(nncoastal(wind,chla,sza,tau,omega,alpha,ozone,B,a,bb)) ## gives IPAR vertical profile upto from 0m to 200m with 2m resolution for coastal waters
