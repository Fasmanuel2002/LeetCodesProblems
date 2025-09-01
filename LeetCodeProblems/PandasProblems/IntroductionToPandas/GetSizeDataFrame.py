import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    #shape == 0 rows and Columns == 1
    return [players.shape[0], players.shape[1]]