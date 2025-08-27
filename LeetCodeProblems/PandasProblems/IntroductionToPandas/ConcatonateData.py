import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatDataFrames = pd.concat(objs=[df1,df2], axis=0)
    return concatDataFrames