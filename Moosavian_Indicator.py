# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 07:56:01 2020

@author: b0589940
"""
import pandas as pd

data_file_path = input("Please paste the file path of the historical stock prices:")

data_file = pd.read_csv(data_file_path)
data_file.dropna(axis=0, inplace=True)

data_file["Pi*Vi"] = data_file["Close"]*data_file["Volume"]
Moosavian_value = data_file["Pi*Vi"].sum()/data_file["Volume"].sum()
start_date = data_file.iloc[0,0]
end_date = data_file.iloc[-1,0]

print("The Moosavian value is " + str(Moosavian_value) + " for the period " + str(start_date) + " to " + str(end_date))