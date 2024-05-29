from sqlite3 import Connection, connect, Cursor
from typing import List, Optional, Tuple, Union

from src.base.logger import logger
from src.type.config import Config
from src.type.types import ReturnType


class SqliteDatabase:
    _connection: Optional[Connection] = None
    _config: Config.DatabaseConfig

    def __init__(self, db_config: Config.DatabaseConfig):
        self._config = db_config

    def _connect(self):
        self._connection = connect(database=self._config.host)

    def get_connection(self) -> Tuple[Connection, Cursor]:
        self._connect()
        return self._connection, self._connection.cursor()

    def run_command(self, query: Union[str, list],
                    args: Optional[Union[tuple, List[tuple]]] = None,
                    return_type: ReturnType = ReturnType.NONE) -> Optional[list]:
        connection, cursor = self.get_connection()
        try:
            if isinstance(query, str):
                query = " ".join(list(filter(lambda x: x != '', query.replace('\n', '').split(" "))))
            else:
                query = map(lambda i: " ".join(list(filter(lambda x: x != '', i.replace('\n', '').split(" ")))), query)
            if isinstance(query, str):
                if args is None:
                    args = tuple()
                logger.trace(f"Executing SQL query: {query}")
                cursor.execute(query, args)
            else:
                if args is None:
                    for item in query:
                        logger.trace(f"Executing SQL query: {item}")
                        cursor.execute(item, tuple())
                else:
                    for item, arg in zip(query, args):
                        logger.trace(f"Executing SQL query: {item}")
                        cursor.execute(item, arg)
            connection.commit()
            match return_type:
                case ReturnType.ALL:
                    return cursor.fetchall()
                case ReturnType.ONE:
                    return cursor.fetchone()
                case ReturnType.NONE:
                    return None
        except Exception as e:
            logger.error(e)
            connection.rollback()
            raise e
        finally:
            cursor.close()
            connection.close()
