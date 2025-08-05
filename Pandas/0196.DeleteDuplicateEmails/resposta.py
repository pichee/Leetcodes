import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person["Duplicado"] = person['email'].duplicated() 
    person.drop(person[person["Duplicado"]==True].index,inplace=True)
    person.drop(columns=["Duplicado"], inplace=True)