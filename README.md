# Kafka Consumer inserting to PostgreSQL

## Table of contents
* [Adding tables](#adding-tables)
* [Run](#run)

## Install requirements



## Adding tables
> :warning: **Inside `new_table.py` can be only one table!**


## Run

### Build docker image

```
cd kafkacons_dbinsert &&
docker build -t db_insert .
```

### Change `./new_table.py` based on instructions inside the file.

### Build container

#### Linux
```

```
#### Windows(cmd)
```
docker run -it -v %cd%\new_table.py:/kafkacons_dbinsert/database/new_table.py db_insert
```

#### To change default parameters just add them at the end e.g. `-t foo --username user`

All parameters are listed bellow:

| Shortcut 	| Full           	| Default       	     |
|----------	|----------------	|---------------	     |
| b_ip     	| bootstrap_ip   	| host.docker.internal   |
| b_p      	| bootstrap_port 	| 9092          	     |
| b_p      	| bootstrap_port 	| 9092          	     |
| g         | group             | None                   |
| t        	| topic          	| sql-insert    	     |
| db_ip    	| database_ip    	| host.docker.internal   |
| db_p     	| database_port  	| 5432          	     |
| db       	| database_name  	| kafkaConsumer 	     |
| user     	| username       	| postgres      	     |
| pass     	| password       	| password      	     |
