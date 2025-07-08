import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    novatabela = pd.merge(employee,employee,left_on='managerId',right_on='id',suffixes=('empregado', 'gerente'))
    novatabela = novatabela[novatabela['salaryempregado']>novatabela['salarygerente']]
    novatabela = novatabela.rename(columns={'nameempregado':'Employee'})
    return novatabela[['Employee']]
