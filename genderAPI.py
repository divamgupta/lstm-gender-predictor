
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.utils.data_utils import get_file
from keras.models import model_from_json

import numpy as np
import random
import sys

print "loading data"

with open("male.txt") as f:
    m_names = f.readlines()

with open("female.txt") as f:
    f_names = f.readlines()

mf_names = []

for f_name in f_names:
	if f_name in m_names:
		mf_names.append(f_name)

m_names = [m_name.lower() for m_name in m_names if not m_name in mf_names]
f_names = [f_name.lower() for f_name in f_names if not f_name in mf_names]


totalEntries = len(m_names) + len(f_names)
maxlen = len(max( m_names , key=len)) + len(max( f_names , key=len))

chars = set(  "".join(m_names) + "".join(f_names)  )
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))


print "total endtries " , totalEntries
print "max len " , maxlen
print('total chars:', len(chars))






with open("model.json", 'r') as content_file:
    json_string = content_file.read()

model = model_from_json(json_string)
print('Model loaded  ')

model.load_weights('my_model_weights.h5')
print('Model weights  ')


def predict(name):
	global maxlen , chars , char_indices
	x = np.zeros((1, maxlen, len(chars)))

	for t, char in enumerate(name):
		x[0, t, char_indices[char]] = 1

	preds = model.predict(x, verbose=0)[0]

	return preds


while True:
	print "enter any name"
	n = raw_input()
	v = predict(n)
	if v[0] > v[1]:
		print "Male"
	else:
		print "Female"

