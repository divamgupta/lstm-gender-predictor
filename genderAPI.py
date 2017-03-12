from keras.models import model_from_json
import numpy as np
import sys


def predict(model, name, maxlen, chars, char_indices):
	x = np.zeros((1, maxlen, len(chars)))
	for t, char in enumerate(name):
		x[0, t, char_indices[char]] = 1

	preds = model.predict(x, verbose=0)[0]
	return preds


def load_model(maleFile, femaleFile):
	mf_names = []
	with open(maleFile) as f:
		m_names = f.readlines()

	with open(femaleFile) as f:
		f_names = f.readlines()

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

	with open("model.json", 'r') as content_file:
		json_string = content_file.read()

	model = model_from_json(json_string)
	model.load_weights('my_model_weights.h5')
	return model, maxlen ,chars ,char_indices


if __name__ == "__main__":
	model, maxlen, chars, char_indices = load_model(sys.argv[1], sys.argv[2])
	while True:
		print "Enter any name:"
		n = raw_input()
		v = predict(model, n, maxlen, chars, char_indices)
		if v[0] > v[1]:
			print "Male"
		else:
			print "Female"
