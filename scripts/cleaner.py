#!/usr/bin/env python

import pandas as pd
import numpy as np

#Sets up the datetime/accession number
def first_cleanse(file):
    df = pd.read_csv(file)
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.set_index(df['datetime'])
    df = df.drop(['date','time','datetime'],axis=1)
    return df


