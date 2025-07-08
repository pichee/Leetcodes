import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    chefes = employee[employee['managerId'].isnull()]
    chefes['managerId'] = chefes['id'] 
    novatabela = pd.merge(employee,chefes ,on ='managerId',how ='inner')
    novatabela = novatabela[novatabela['salary_x']>novatabela['salary_y']]
    novatabela = novatabela.rename(columns={'name_x':'Employee'})
    return novatabela[['Employee']]
