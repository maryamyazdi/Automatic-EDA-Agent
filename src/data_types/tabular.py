import pandas as pd


class TabularData:
    def __init__(self, path: str):
        if not path.endswith("csv") and not path.endswith("xlsx"):
            raise ValueError(
                f'Expected a csv or excel file, but got {path.split(".")[-1]} instead!'
            )
        self.data = pd.read_csv(path) if path.endswith("csv") else pd.read_excel(path)

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return not self.data.empty

    def __getitem__(self, row_index: int):
        return self.data[row_index, :]
