import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "postgresql://postgres:test@localhost:5432/esg"
DEFAULT_TABLE = "scores"


class DatabaseConnector:
    def __init__(self):
        self.engine = create_engine(DB_PATH)
        self.table_names = pd.read_sql(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            """,
            self.engine,
        )

    def fetch_data(self, table=DEFAULT_TABLE) -> pd.DataFrame:
        return pd.read_sql_table(table, self.engine)

    def store_data(self, df, table=DEFAULT_TABLE) -> None:
        df.to_sql(table, self.engine, if_exists="replace", index=False, chunksize=100)
        return None
