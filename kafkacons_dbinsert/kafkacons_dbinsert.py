import json
import os
from kafka import KafkaConsumer


from database import db
from utils import DB_CONN_URL, GROUP_ID, BOOTSTRAP_SERVER_ADDR, TOPIC_NAME


db.connect(DB_CONN_URL)
db.load_table('database')
table_object = list(db.Base._decl_class_registry.values())[0]
db.create_table()

print(f">>> Connecting kafka..."
      f"BOOTSTRAP_SERVER_ADDR: {BOOTSTRAP_SERVER_ADDR}"
      f"TOPIC: {TOPIC_NAME}"
      f"GROUP_ID: {GROUP_ID}")

consumer = KafkaConsumer(TOPIC_NAME,
                         group_id=GROUP_ID,
                         bootstrap_servers=[BOOTSTRAP_SERVER_ADDR],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

print(f">>> Kafka connected.")
print(f">>> Consuming messages...")

for message in consumer:
    db.insert(**message.value)
# TODO: pwd