import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Kafka consumer inserting data to PostgreSQL")

    parser.add_argument('--bootstrap_server', default='host.docker.internal:9092')
    parser.add_argument('--group_id', default=None)
    parser.add_argument('--topic', default='example.001')

    parser.add_argument('--db_ip', default='host.docker.internal')
    parser.add_argument('--db_port', default='5432')
    parser.add_argument('--db_name', default='postgres')
    parser.add_argument('--db_username', default='postgres')
    parser.add_argument('--db_password', default='password')

    return parser


def postgres_uri(username, password, ip, port, db_name):
    return f'postgresql+psycopg2://{username}:{password}@{ip}:{port}/{db_name}'
