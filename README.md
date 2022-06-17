* Model

Usemodels.py file contains both models.

The necessary packages to install and import are Tensorflow, sklearn (Pickle), Numpy and H5py.
's1nniparopen.h5' is Neural network model for open ocean and 's1tnniparcoastal.h5' is for coastal waters.
The pickle files with name including 'inputscalar' contains normalizing scalars from input parameters in training input dataset, and with name including 'outputstd' are standard deviation of output parameter in training dataset. These files are used during the prediction.
usemodels.py gives the prediction of IPAR(0^-),K_1 and K_2 and hence the vertical profile of IPAR under different atmospheric and oceanic condition.
Users can change the values of input parameters with in the given range as required
To test the models performance in user environment, please check the benchmark test cases and their prediction results as listed in 'Test cases to check model performance in users' environment.docx' file.
All files must be in the same directory.
