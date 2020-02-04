#!/usr/bin/env python

import pandas as pd
import numpy as np

def filterer(file,threshold):
    	df = pd.read_csv(file) 
	df['Counts'] = (df.groupby(['datetime'])['accession'].transform('count'))
    	df['Normalized'] = (df['Counts']-min(df['Counts'])) / (max(df['Counts']) - min(df['Counts']))
    	return df[df['Normalized'] > threshold]
