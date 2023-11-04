# monte_carlo_producer.py
from kafka import KafkaProducer
import random
import time
import logging


logger = logging.getLogger(__name__)
# Set up a Kafka producer
producer = KafkaProducer(bootstrap_servers="kafka:9092", api_version=(0, 11, 5))


# Simulate Monte Carlo alerts
def generate_alerts():
    alerts = [
        "Alert 1: Data reliability issue detected.",
        "Alert 2: Table health concern identified.",
        "Alert 3: Anomaly detected in column X.",
    ]

    while True:
        alert = random.choice(alerts)
        try:
            alert_bytes = alert.encode("utf-8")
            producer.send("monte_carlo_alerts", value=alert_bytes)
            print(f"Sent: {alert}")
            logger.info(f"Sent: {alert}")
        except Exception as e:
            logger.error(str(e))
            print(f"Error sending alert: {e}")
        time.sleep(random.uniform(1, 5))  # Simulate random time intervals


if __name__ == "__main__":
    generate_alerts()
