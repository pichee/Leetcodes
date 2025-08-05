import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    lista_dias = weather[['id','recordDate','temperature']].values.tolist()
    Resposta = pd.DataFrame(columns=['id'])
    contador = 0
    tmd = len(lista_dias)
    tmd = tmd - 1
    for dia in range(tmd):
        if lista_dias[dia+1][2]>lista_dias[dia][2] and lista_dias[dia+1][1]-lista_dias[dia][1]==timedelta(days=1):
            Resposta.loc[contador]=lista_dias[dia+1][0]
            contador+=1
    return Resposta

