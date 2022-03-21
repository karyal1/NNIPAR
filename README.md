The necessary packages to install and import are Keras, Pickle, Numpy, H5py.
nniparopen.h5 is Neural model for open ocean and nniparcoastal.h5 is for coastal waters.
The pickle files with name starting 'inputscalar' contains normalizing scalars from input parameters in training input dataset, and with name starting 'outputstd' are standard deviation of output parameter in training dataset. These files are used during the prediction.
usemodels.py gives the prediction of IPAR(0^-),K_1 and K_2 and hence the vertical profile of IPAR under different atmospheric and oceanic condition.
