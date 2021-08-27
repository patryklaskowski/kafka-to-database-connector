import json
import os
from kafka import KafkaConsumer
print("curdir: ", os.path.abspath(os.curdir))

from database import db
from utils import DB_CONN_URL, BOOTSTRAP_SERVER_ADDR, TOPIC_NAME


db.connect(DB_CONN_URL)
db.load_table('database')
table_object = list(db.Base._decl_class_registry.values())[0]
db.create_table()

# TODO: Add GroupID
consumer = KafkaConsumer(TOPIC_NAME,
                         bootstrap_servers=[BOOTSTRAP_SERVER_ADDR],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    db.insert(**message.value)
