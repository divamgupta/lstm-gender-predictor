# Simple LSTM based Gender Predictor 
Predict the gender of a name using LSTM

Requirements:
* keras
* h5py

## How to use :

To train the model:

`THEANO_FLAGS=device=gpu,floatX=float32 python train_genders.py`

Command to see test the trained results:

`python genderAPI.py <male_textfile> <female_textfile>` 
