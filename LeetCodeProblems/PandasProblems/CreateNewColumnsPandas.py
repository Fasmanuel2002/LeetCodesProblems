import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    #me complique la existencia
    employees["bonus"] = employees["salary"] * 2
    return employees
    