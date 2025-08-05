import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
        TabelaDosMerge = pd.merge(sales_person,orders,right_on='sales_id',left_on='sales_id',how='left')
        TabelaDosMerge = TabelaDosMerge[['sales_id','name','com_id']]
        TabelaDosMerge = pd.merge(TabelaDosMerge,company,right_on='com_id',left_on='com_id',how='left')
        lista = TabelaDosMerge[TabelaDosMerge['name_y']=='RED']
        lista = lista['name_x'].tolist()
        TabelaDosMerge = TabelaDosMerge[~TabelaDosMerge['name_x'].isin(lista)]
        TabelaDosMerge = TabelaDosMerge.rename(columns={'name_x': 'name'})
        TabelaDosMerge.drop_duplicates(subset=['name'],inplace=True)
        return TabelaDosMerge[['name']]