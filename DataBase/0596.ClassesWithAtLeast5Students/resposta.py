import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count().reset_index(name='total_alunos')
    courses = courses[courses['total_alunos'] >= 5]
    return courses[['class']]