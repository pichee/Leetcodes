import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    tabela = pd.merge(employee,bonus,how="left")
    tabela = tabela[(tabela["bonus"]<1000) | (tabela["bonus"].isnull())]
    tabela = tabela[['name','bonus']]
    return tabela