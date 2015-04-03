sleep 2
echo "setting up postgres database:$DBNAME"
psql -U postgres -h $DBHOST -c "create database $DBNAME"
psql -U postgres -h $DBHOST -d mydb -c "create extension hstore"
python -c "import data; date.setup()"
