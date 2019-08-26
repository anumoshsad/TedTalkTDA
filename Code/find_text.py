# has to run with python 2 

import pickle
import glob
import os

files_path = glob.glob('/Users/Shouman/Downloads/Data/Rupam_MachineLearning/Ted_data/TED_meta/*.pkl')

def find_text(file):
	
	with open( file, "rb" ) as f:
		data = pickle.load(f)
	d = dict()
	d['transcript'] = data['talk_transcript']
	d['title'] = data['talk_meta']['title']
	d['id'] = data['talk_meta']['id']
	
	name = os.path.basename(file)
	path = '../Data/' + name
	with open(path,"wb") as f:
		pickle.dump(d, f)
	return



for File in files_path:
	find_text(File)
	
