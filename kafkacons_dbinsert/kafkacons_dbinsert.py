import json
import os
from kafka import KafkaConsumer


from database import db
from utils import DB_CONN_URL, GROUP_ID, BOOTSTRAP_SERVER_ADDR, TOPIC_NAME


db.connect(DB_CONN_URL)
db.load_table('database')
table_object = list(db.Base._decl_class_registry.values())[0]
db.create_table()

print(f">>> Connecting kafka...\n"
      f"    BOOTSTRAP_SERVER_ADDR: {BOOTSTRAP_SERVER_ADDR}\n"
      f"    TOPIC: {TOPIC_NAME}\n"
      f"    GROUP_ID: {GROUP_ID}\n")

consumer = KafkaConsumer(TOPIC_NAME,
                         group_id=GROUP_ID,
                         bootstrap_servers=[BOOTSTRAP_SERVER_ADDR],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

print(f">>> Kafka CONNECTED.")
print(f">>> Consuming messages")
print("." * 40 + "\n")

for message in consumer:
    db.insert(**message.value)
