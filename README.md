* Algorithm Package
  -  This package contains two neural network (NN) models one for open ocean and another for coastal waters.
  - The NN models predict three parameters: IPAR just below the surface(IPAR(0),K1 and K2).
  - The input parameters to open ocean NN model are windspeed,chla,sza,aod,ssa,aa and ozone.
  - The input parameters to coastal waters NN model are windspeed,chla,sza,aod,ssa,aa,ozone,B(670),a(490),bb(490).
* Dependency (needs install and imports)
  - Tensorflow
  - pandas
  - numpy
  - pickle
  - os
  - fnmatch
  - sys
* Using the package
  - Download the package. All files must be in the same directory.
  - To check models' performance in users environment run 'testmodels.py' script using command: python3 testmodels.py. The output from this run       will have two csv files: 'test_open.csv' and 'test_coastal.csv' for open ocean model and coastal waters model respectively. CSV files will         have the predicted values of IPAR(0),K1 and K2 along with their reference values Ref(IPAR(0)),Ref(K1) and Ref(K2) respectively. If predicted       values match with reference values, then application of models in user's environment can be confirmed.
  - To use models for prediction run 'usemodels.py'. This script gives different csv files according to user's need.
  - Modify input parameters in usemodels.py file to get desired output. It has mainly three functions: NN model for open ocean, NN model for           coastal waters, function to give vertical profile of IPAR. 
