# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:39:41 2022

@author: kamal
"""
import models as m
import numpy as np



##Users can adjust the value of different input parameters within the given range as needed.
##The parameters B, a, and bb are used only for coastal waters NN model.
## Function nnopen() and nncoastal() are NN model for open ocean and coastal waters respectively which give prediction of surface IPAR(IPAR(0)), K_1,K_2 in a csv file.
## function verticalprofile(x,z) takes output from NN model's output and array of depths as input and gives IPAR vertical profile for corresponding case in a csv file.

##----------------Input parameters for individual case-----------##
wind=4          ##wind speed (m/s), range=(0.5-10)
chla=0.1        ##chla(mg/m3), range=(0.001,30)
sza=74          ##sza(degrees), range=(0,82)
tau=0.4         ##Extinction Aerosol optical depth, range=(0,0.5)
omega=0.9       ##single scattering albedo, range=(0.88,0.99)
alpha=1         ##angstrom exponent, range=(-0.06,1.45)
ozone=400       ##Ozone column (dobson unit), range=(150,450)
B=0.05          ##Backscattering fraction at 670 nm (unitless), range=(0.002,0.05)
a=0.25          ##absorption coefficient at 490 nm (m^-1), range=(0.015-1.274)
bb=0.075        ##backscattering coefficient at 490 (m^-1),range=(0.001-0.116)

opendata=np.array([wind,chla,sza,tau,omega,alpha,ozone])
coastaldata=np.array([wind,chla,sza,tau,omega,alpha,ozone,B,a,bb])


##-----------------Input parameters for group cases-------##
##To get prediction on group of cases simultaneously, users should give 2d array of input parameters on order to NN models 
## for open ocean the array element should be on order [wind,chla,sza,tau,omega,alpha,ozone]
## for coastal waters the array elements should be on order [wind,chla,sza,tau,omega,alpha,ozone,B,a,bb]
odata=np.array([[8,2,30,0.3,0.95,1.3,350],[4,0.1,74,0.4,0.9,1,400],[2,10,55,0.1,0.97,0.5,380]])
cdata=np.array([[8,2,30,0.3,0.95,1.3,350,0.01,1.1,0.1],[4,0.1,74,0.4,0.9,1,400,0.05,0.25,0.075],[2,10,55,0.1,0.97,0.5,380,0.03,0.6,0.5]])

##-----------Using NN models for individual cases-------------###
m.nnopen(opendata)                             ##gives csv file with name starting 'open' 
m.nncoastal(coastaldata)                       ##gives csv file with name starting 'Coastal'
m.verticalprofile(m.nnopen(opendata),np.arange(1,50,1)) ##gives csv file with name starting 'Vertical_ProfileOpen'
m.verticalprofile(m.nncoastal(coastaldata),np.arange(1,50,1))##gives csv file with name starting 'Vertical_ProfileCoastal'

##-----------Using NN models for group cases-------------###
m.nnopen(odata)                             ##gives csv file with name starting 'open' 
m.nncoastal(cdata)                       ##gives csv file with name starting 'Coastal'
m.verticalprofile(m.nnopen(odata),np.arange(1,50,1)) ##gives csv file with name starting 'Vertical_ProfileOpen'
m.verticalprofile(m.nncoastal(cdata),np.arange(1,50,1))##gives csv file with name starting 'Vertical_ProfileCoastal'
