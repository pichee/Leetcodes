import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    clientesPedido = pd.merge(orders,customers,right_on='id',left_on='customerId',how='inner')
    resposta = customers[~customers['id'].isin(clientesPedido['customerId'])]
    resposta = resposta.rename(columns={'name':'Customers'})
    return resposta[['Customers']]
