import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
   novoDataframe = person.copy()
   novoDataframe["Verificador"] = person['email'].duplicated()
   novoDataframe = novoDataframe[novoDataframe['Verificador'] == True]
   novoDataframe = novoDataframe.rename(columns={'email':'Email'})
   novoDataframe = novoDataframe.drop_duplicates(subset='Email')
   return novoDataframe[['Email']]
