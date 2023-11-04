# monte_carlo_consumer.py
from kafka import KafkaConsumer
from cassandra.cluster import Cluster

# Set up a Kafka consumer
consumer = KafkaConsumer(
    "monte_carlo_alerts",
    bootstrap_servers="kafka:9092",
    group_id="monte_carlo_group",
    api_version=(0, 11, 5),
)

# Set up a Cassandra connection
cluster = Cluster(["cassandra"])
session = cluster.connect()
session.execute(
    "CREATE KEYSPACE IF NOT EXISTS alerts WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1}"
)
session.execute(
    "CREATE TABLE IF NOT EXISTS alerts.alerts (id UUID PRIMARY KEY, message text)"
)

# Consume and store alerts
for msg in consumer:
    alert = msg.value.decode("utf-8")
    session.execute(
        "INSERT INTO alerts.alerts (id, message) VALUES (uuid(), %s)", (alert,)
    )
    print(f"Received: {alert}")

cluster.shutdown()
