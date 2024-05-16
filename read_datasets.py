import pandas as pd

data = pd.read_csv('datasets/diabetes.csv',skiprows=3,
                   names=["Preg","Plas","Pres","skin","test","mass","pedi","age","class"])
reqs = pd.read_table(r'E:\New folder\machine_learning\datasets\requirements.txt')
data_xls = pd.read_excel('datasets/diabetes.xls')

