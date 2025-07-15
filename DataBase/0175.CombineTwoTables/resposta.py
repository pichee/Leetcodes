import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
   merge = pd.merge(person,address , on='personId',how ='left')
   resultado = merge[['firstName','lastName','city','state']]
   return resultado