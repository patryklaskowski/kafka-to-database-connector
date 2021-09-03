# TO BE UPDATED....

# Kafka Consumer inserting to PostgreSQL

## Table of contents
* [Requirements](#requirements)
* [Run](#run)

## Requirements
 1. PostgreSQL 9.4.24 or newer
 2. Apache Kafka 2.8.0
 3. Apache ZooKeeper 3.6.3
 4. Docker 20.10.8 or newer

## Run

### 1. Build docker image

```
cd kafkacons_dbinsert &&
docker build -t db_insert .
```

### 2. Change `./new_table.py` based on instructions inside the file.

### 3. Run container

#### Linux
```
docker run -it -v "$PWD"/"new_table.py":/kafkacons_dbinsert/database/new_table.py db_insert
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
