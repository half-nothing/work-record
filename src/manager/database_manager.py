from src.base.config import config
from src.module.sqlite_database import SqliteDatabase

database = SqliteDatabase(config.config.database)
database.run_command(
    [
        """
        CREATE TABLE IF NOT EXISTS "location" (
          "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "address" TEXT NOT NULL,
          "remark" TEXT DEFAULT ''
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS "record" (
          "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          "location_id" INTEGER NOT NULL,
          "time" integer NOT NULL,
          "year" integer NOT NULL,
          "month" integer NOT NULL,
          "day" integer NOT NULL,
          CONSTRAINT "location_key" 
          FOREIGN KEY ("location_id") 
          REFERENCES "location" ("id") 
          ON DELETE RESTRICT 
          ON UPDATE RESTRICT
        );
        """
    ]
)
