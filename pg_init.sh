echo "setting up postgres database:$DBNAME"
psql -U postgres -h $DBHOST -c "create database $DBNAME"
psql -U postgres -h $DBHOST -d $DBNAME -c "create extension hstore"

sleep 2
python -c "import data; data.setup()"
