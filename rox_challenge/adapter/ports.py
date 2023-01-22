from abc import ABC, abstractmethod
import pandas as pd
from typing import Dict


class Source(ABC):
    """Abstract class to define input data and return a pandas DataFrame."""

    @abstractmethod
    def read(self) -> Dict[str, pd.DataFrame]:
        pass


class TargetDB(ABC):
    """Abstract class to define target data."""

    @abstractmethod
    def write(self, dataframe: pd.DataFrame, table_name: str) -> None:
        pass
