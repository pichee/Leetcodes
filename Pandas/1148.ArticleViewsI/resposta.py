import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    novatabela = views[views['author_id'] == views['viewer_id']]
    novatabela = novatabela[['author_id']].drop_duplicates()
    novatabela = novatabela.rename({'author_id':'id'},axis = 1)
    novatabela = novatabela.sort_values(by='id')
    return novatabela
