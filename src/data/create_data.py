#!/usr/bin/env python

import sys

from joblib import Parallel, delayed
import multiprocessing

import pandas as pd
import numpy as np

import pickle
from create_images import CTScan


def create_data(idx, outDir, width = 50):
	'''
	Generates your test, train, validation images
	outDir = a string representing destination
	width (int) specify image size
	'''
	scan = CTScan(np.asarray(X_data.loc[idx])[0], \
		np.asarray(X_data.loc[idx])[1:])
	outfile = outDir  +  str(idx)+ '.tiff'
	scan.save_image(outfile, width)

mode = sys.argv[1]
inpfile = mode + 'data'
outDir = mode + '/image_'
X_data = pd.read_pickle(inpfile)


# Parallelizes inorder to generate more than one image at a time
Parallel(n_jobs = 3)(delayed(create_data)(idx, outDir) for idx in X_data.index)
