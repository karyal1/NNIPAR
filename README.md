The necessary packages to install and import are Keras, Pickle, Numpy and H5py.
's1nniparopen.h5' is Neural model for open ocean and 's1tnniparcoastal.h5' is for coastal waters.
The pickle files with name including 'inputscalar' contains normalizing scalars from input parameters in training input dataset, and with name including 'outputstd' are standard deviation of output parameter in training dataset. These files are used during the prediction.
usemodels.py gives the prediction of IPAR(0^-),K_1 and K_2 and hence the vertical profile of IPAR under different atmospheric and oceanic condition.
All files must be in the same directory.
