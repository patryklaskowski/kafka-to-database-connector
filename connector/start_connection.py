import json

from kafka import KafkaConsumer

from utils import create_parser, postgres_uri
from database.database import Database
from database.new_table import BaseClass


parser = create_parser()
args = parser.parse_args()

postgres = postgres_uri(args.db_username, args.db_password, args.db_ip, args.db_port, args.db_name)

# Connect to database, load a
db = Database.from_uri(postgres, base=BaseClass)
db.load_table_from(table_dir='database')
db.create_loaded_table()

config = dict(group_id=args.group_id,
              bootstrap_servers=[args.bootstrap_server],
              value_deserializer=lambda m: json.loads(m.decode('utf-8')),
              max_in_flight_requests_per_connection=1,
              enable_auto_commit=True,
              consumer_timeout_ms=float('inf'),  # Never raises StopIteration
              auto_offset_reset='earliest')

for key, value in config.items():
    print(f'{key}={value}')

consumer = KafkaConsumer(args.topic, **config)

try:

    for message in consumer:
        success = db.insert(**message.value)

except BaseException as e:
    raise Exception('Unexpected exception') from e
finally:
    print('Closing consumer')
    consumer.close(autocommit=True)

print('Done!')
