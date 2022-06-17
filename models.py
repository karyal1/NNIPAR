import pickle
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import time
import os
import fnmatch as fm
from sys import argv
start = time.process_time()
import warnings

def load(x):
    with warnings.catch_warnings():
          warnings.simplefilter("ignore", category=UserWarning)
          return pickle.load(open(x,'rb'))

def nnopen(oinput):
    directory =os.path.basename(argv[0])
    a1=list()
    model_open = load_model('s1nniparopen.h5',compile=None)
    inputscalar_open = load('sinputscalaropen.pkl')
    outputscalar_open=load('soutputstdopen.pkl')
    if oinput.ndim==1:
        values=np.array([oinput])
    else:
        values=oinput
    filestrbase='Open_Wind%.1f'% values[0][0]\
                    +'_Chla%.2f' % values[0][1]\
                    +'_SZA%.1f' %  values[0][2]\
                    +'_AOD%.2f' % values[0][3]\
                    +'_SSA%.2f' % values[0][4]\
                    +'_AA%.2f' % values[0][5]\
                    +'_Ozone%.1f' % values[0][6]
    if oinput.ndim==1:
        Xopen=inputscalar_open.transform([oinput])
        a2=outputscalar_open.inverse_transform(model_open([Xopen])).flatten()
        a3=oinput.tolist()+a2.tolist()
        a1.append(a3)
    else:
        for i in range (oinput.shape[0]):
            Xopen=inputscalar_open.transform([oinput[i,:]])
            a2=outputscalar_open.inverse_transform(model_open([Xopen])).flatten()
            a3=oinput[i,:].tolist()+a2.tolist()
            a1.append(a3)
    

    df=pd.DataFrame(a1,columns=['Wind', 'Chla', 'SZA', 'AOD', 'SSA','AA','Ozone',r'IPAR(0)','K1','K2'])
    if fm.fnmatch(directory,'testmodels.py'):
        a4=[[130.8275146,0.040552534,0.398340821],[1325.746582,0.241900459,0.200544834],[1065.5,0.492925197,0.37158072]]
        df1=pd.DataFrame(a4,columns=['Ref(IPAR(0))','Ref(K1)','Ref(K2)'])
        df2=pd.concat([df, df1], axis=1)
        return [np.array(a1),df,filestrbase,df2.to_csv('test_open.csv',index=False)]
    else:
        return [np.array(a1),df,filestrbase,df.to_csv(filestrbase+'.csv', index=False)]           
    
def nncoastal(cinput):
    directory =os.path.basename(argv[0])
    a1=list()
    model_coastal = load_model('s1tnniparcoastal.h5',compile = False)
    inputscalar_coastal = load('s1tinputscalarcoastal.pkl')
    outputscalar_coastal=load('s1toutputstdcoastal.pkl')
    if cinput.ndim==1:
        values=np.array([cinput])
    else:
        values=cinput
    filestrbase='Coastal_Wind%.1f'% values[0][0]\
                    +'_Chla%.2f' % values[0][1]\
                    +'_SZA%.1f' %  values[0][2]\
                    +'_AOD%.2f' % values[0][3]\
                    +'_SSA%.2f' % values[0][4]\
                    +'_AA%.2f' % values[0][5]\
                    +'_Ozone%.1f' % values[0][6]\
                    +'_B%.2f' % values[0][7]\
                    +'_a%.2f' % values[0][8]\
                    +'_bb%.2f' % values[0][9]
    if cinput.ndim==1:
        Xcoastal=inputscalar_coastal.transform([cinput])
        a2=outputscalar_coastal.inverse_transform(model_coastal([Xcoastal])).flatten()
        a3=cinput.tolist()+a2.tolist()
        a1.append(a3)
    else:
        for i in range (cinput.shape[0]):
            Xcoastal=inputscalar_coastal.transform([cinput[i,:]])
            a2=outputscalar_coastal.inverse_transform(model_coastal([Xcoastal])).flatten()
            a3=cinput[i,:].tolist()+a2.tolist()
            a1.append(a3)
    df=pd.DataFrame(a1,columns=['Wind', 'Chla', 'SZA', 'AOD', 'SSA','AA','Ozone','B(670)','a(490)','bb(490)',r'IPAR(0)','K1','K2'])
    if fm.fnmatch(directory,'testmodels.py'):
        a4=[[144.3686676,-0.004072354,1.782362103],[1389.579712,0.241554797,2.311629534],[833.2581787,0.747719944,3.318435907]]
        df1=pd.DataFrame(a4,columns=['Ref(IPAR(0))','Ref(K1)','Ref(K2)'])
        df2=pd.concat([df, df1], axis=1)
        return [np.array(a1),df,filestrbase,df2.to_csv('test_coastal.csv',index=False)]
    else:
        return [np.array(a1),df,filestrbase,df.to_csv(filestrbase+'.csv', index=False)]          
def verticalprofile(x,z):
    a1=list()
#    z=np.arange(0,201,2)
    a2=x[0]
    df1=x[1]
    filestrbase=x[2]

    if a2.shape[0]==1:
        a2=a2[0]
        iparz=a2[-3]*np.exp(-a2[-2]*z)*np.exp(-a2[-1]*z/(z+1)**0.5)
        a3=iparz.tolist()
        a1.append(a3)
    else:
        for i in range (a2.shape[0]):
            a4=a2[i,:]
            iparz=a4[-3]*np.exp(-a4[-2]*z)*np.exp(-a4[-1]*z/(z+1)**0.5)
            a3=iparz.tolist()
            a1.append(a3)
    df2=pd.DataFrame(a1,columns=[str('IPAR(')+(str(i)+str('m)')) for i in z])
    df3=pd.concat([df1, df2], axis=1)
    return df3.to_csv('Vertical_Profile'+filestrbase+'.csv', index=False)
        