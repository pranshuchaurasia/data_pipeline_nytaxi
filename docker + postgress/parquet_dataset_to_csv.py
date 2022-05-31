#!/usr/bin/env python
# coding: utf-8
#Implemented in Jupyter notebook
#Converting Jupyter notebook into py format : jupyter nbconvert parquet_dataset_to_csv.ipynb --to python

#Note that Ny-taxi dataset does not have dataset in csv format, so it neets to be converted into csv using pandas.
import pandas as pd

#Reading the parquet file
df = pd.read_parquet('C:\docker\data_engineering_bootcamp\week1\docker_sql\yellow_tripdata_2021-01.parquet')

#converting the file to csv
df.to_csv('yellow_tripdata_2021-01.csv')

#reading the csv file
dk = pd.read_csv('yellow_tripdata_2021-01.csv')

#Validating if all the columns are loaded successfully or not.
dk



