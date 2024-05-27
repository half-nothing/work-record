class Config:
    class DatabaseConfig:
        host: str
        password: str
        username: str
        database_name: str
        port: int
        auto_commit: bool
        ping_delay: int
        database_type: str

        def __init__(self, data: dict):
            self.__dict__ = data

    config_version: str
    database: DatabaseConfig | dict

    def __init__(self, data: dict):
        self.__dict__ = data
        self.database = self.DatabaseConfig(self.database)
