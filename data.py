import os
from playhouse.postgres_ext import Model, PostgresqlExtDatabase, JSONField

DB_NAME = os.environ["DBNAME"]
DB_HOST = os.environ["DBHOST"]
DB_USER = os.environ["DBUSER"]
DB = PostgresqlExtDatabase(DB_NAME, host=DB_HOST, user=DB_USER)

class Doc(Model):
   data = JSONField() 
   class Meta:
       database = DB

def setup():
    Doc.create_table()

if __name__ == '__main__':
    pass
