# app.py
from flask import Flask, render_template
from kafka import KafkaConsumer
from cassandra.cluster import Cluster

app = Flask(__name__)


def fetch_alerts_from_cassandra():
    cluster = Cluster(["cassandra"])
    session = cluster.connect()
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS alerts WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1}"
    )
    session.execute(
        "CREATE TABLE IF NOT EXISTS alerts.alerts (id UUID PRIMARY KEY, message text)"
    )
    result = session.execute("SELECT message FROM alerts.alerts")
    alerts = [row.message for row in result]
    cluster.shutdown()
    return alerts


@app.route("/")
def display_alerts():
    alerts = fetch_alerts_from_cassandra()
    return render_template("alerts.html", alerts=alerts)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
