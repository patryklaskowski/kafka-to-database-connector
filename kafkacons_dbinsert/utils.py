import argparse

parser = argparse.ArgumentParser(description="Kafka consumer inserting data to PostgreSQL")
parser.add_argument('-b_ip', '--bootstrap_ip', default='host.docker.internal')
parser.add_argument('-b_p', '--bootstrap_port', default='9092')
parser.add_argument('-g', '--group_id', default=None)
parser.add_argument('-t', '--topic', default='sql-insert')
parser.add_argument('-db_ip', '--database_ip', default='host.docker.internal')
parser.add_argument('-db_p', '--database_port', default='5432')
parser.add_argument('-db', '--database_name', default='kafkaConsumer')
parser.add_argument('-user', '--username', default='postgres')
parser.add_argument('-pass', '--password', default='password')

args = parser.parse_args()

GROUP_ID = args.group_id

BOOTSTRAP_SERVER_ADDR = f"{args.bootstrap_ip}:{args.bootstrap_port}"

TOPIC_NAME = args.topic

DB_CONN_URL = \
    f'postgresql+psycopg2://{args.username}:{args.password}@{args.database_ip}:{args.database_port}/{args.database_name}'