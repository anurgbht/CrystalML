import pandas as pd
from pathlib import Path

PARENT_DIR = Path(__file__).parent.parent
INPUT_DIR = Path(PARENT_DIR,'input')

INTERESTING_COLUMNS = ['a','b','c','alpha','beta','gamma','sg']

def read_xlsx(fpath):
    df = pd.read_excel(fpath)
    return df

def modify_df(df):
    modified_df = df[INTERESTING_COLUMNS]
    modified_df = modified_df[modified_df.alpha == 90].reset_index(drop=1)
    modified_df = modified_df[modified_df.beta == 90].reset_index(drop=1)
    modified_df = modified_df[modified_df.gamma == 90].reset_index(drop=1)

    print(modified_df.sample(5))
    print(modified_df.shape)
    print(len(modified_df.sg.unique()))
    return modified_df

if __name__ == "__main__":
    fpath = Path(INPUT_DIR,'Data.xlsx')
    raw_df = read_xlsx(fpath)
    subset_df = modify_df(raw_df)