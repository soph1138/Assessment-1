import pandas as pd
import numpy as np

database_service = "sqlite"
database = "jupiter.db"
moons_db = pd.read_sql_table('moons', 'sqlite:///jupiter.db')

class Moons:
    def __init__(self,dataset):
        self.dataset = moons_db
    def data_shape(self):
        self.data_shape = moons_db.shape
    def data_size(self):
        self.data_size = moons_db.size
    def col_names(self):
        for col in moons_db.columns:
            print(col)
    def describe_data(self):
        self.describe_data = moons_db.describe()
    def corr_matrix(self):
        self.corr_matrix = moons_db.corr(numeric_only=True)
    def col_data(self,column):
        self.col_data = moons_db[column]
    def moon_data(self,name):
        self.moon_data = moons_db.loc[moons_db['moon'] == name]
