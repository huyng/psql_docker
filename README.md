Docker + Postgres + Python

### Setup

```

# start postgres service
docker-compose up

# create db and tables
docker-compose run shell /bin/sh pg_init.sh
```


### Interacting with the database

```
docker-compose run shell ipython
```

```
from data import Doc

# create a new document and insert into postgres
d1 = Doc.create(data={"name":"foobar", food":"chocolate"})
d2 = Doc.create(data={"name":"barfoo", food":"carrot"})

# query for document(s)

results = Doc.select().where(Doc.data["food"] == "carrot")
for doc in results:
    print doc.id, doc.data

```

### Saving postgres db data

```
docker-compose run shell /bin/sh pg_dump.sh
```

### Loading postgres db data

```
docker-compose run shell /bin/sh pg_load.sh
```

### Run example

`example.py` is a program that will insert fake data into postgres and demonstrate a few queries using the data.

```
docker-compose run shell python example.py
```

