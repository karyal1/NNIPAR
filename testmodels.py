# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:08:23 2022

@author: kamal
"""
import models as m
import numpy as np

##There are three test cases for open ocean and three for coastal waters.
##Running this script produces an csv file with model's prediction and reference values.
##If the prediction and reference values match then the models are good in users' environment

###**----------------test1------------
wind1=4          ##wind speed (m/s), range=(0.5-10)
chla1=0.1        ##chla(mg/m3), range=(0.001,30)
sza1=74          ##sza(degrees), range=(0,82)
aod1=0.4         ##Extinction Aerosol optical depth, range=(0,0.5)
ssa1=0.9       ##single scattering albedo, range=(0.88,0.99)
aa1=1         ##angstrom exponent, range=(-0.06,1.45)
ozone1=400       ##Ozone column (dobson unit), range=(150,450)
B1=0.05          ##Backscattering fraction at 670 nm (unitless), range=(0.002,0.05)
a1=0.25          ##absorption coefficient at 490 nm (m^-1), range=(0.015-1.274)
bb1=0.075        ##backscattering coefficient at 490 (m^-1),range=(0.001-0.116)

otest1=[wind1,chla1,sza1,aod1,ssa1,aa1,ozone1]
ctest1=[wind1,chla1,sza1,aod1,ssa1,aa1,ozone1,B1,a1,bb1]
###**----------------test2------------
wind2=8          ##wind speed (m/s), range=(0.5-10)
chla2=2        ##chla(mg/m3), range=(0.001,30)
sza2=30          ##sza(degrees), range=(0,82)
aod2=0.3         ##Extinction Aerosol optical depth, range=(0,0.5)
ssa2=0.95       ##single scattering albedo, range=(0.88,0.99)
aa2=1.3         ##angstrom exponent, range=(-0.06,1.45)
ozone2=350       ##Ozone column (dobson unit), range=(150,450)
B2=0.01          ##Backscattering fraction at 670 nm (unitless), range=(0.002,0.05)
a2=1.1          ##absorption coefficient at 490 nm (m^-1), range=(0.015-1.274)
bb2=0.1        ##backscattering coefficient at 490 (m^-1),range=(0.001-0.116)

otest2=[wind2,chla2,sza2,aod2,ssa2,aa2,ozone2]
ctest2=[wind2,chla2,sza2,aod2,ssa2,aa2,ozone2,B2,a2,bb2]
###**----------------test3------------
wind3=2          ##wind speed (m/s), range=(0.5-10)
chla3=10        ##chla(mg/m3), range=(0.001,30)
sza3=55          ##sza(degrees), range=(0,82)
aod3=0.1         ##Extinction Aerosol optical depth, range=(0,0.5)
ssa3=0.97       ##single scattering albedo, range=(0.88,0.99)
aa3=0.5         ##angstrom exponent, range=(-0.06,1.45)
ozone3=380       ##Ozone column (dobson unit), range=(150,450)
B3=0.03          ##Backscattering fraction at 670 nm (unitless), range=(0.002,0.05)
a3=0.6          ##absorption coefficient at 490 nm (m^-1), range=(0.015-1.274)
bb3=0.5        ##backscattering coefficient at 490 (m^-1),range=(0.001-0.116)

otest3=[wind3,chla3,sza3,aod3,ssa3,aa3,ozone3]
ctest3=[wind3,chla3,sza3,aod3,ssa3,aa3,ozone3,B3,a3,bb3]

otest=np.array([otest1,otest2,otest3])
ctest=np.array([ctest1,ctest2,ctest3])
m.nncoastal(ctest)
m.nnopen(otest)