from google.cloud import pubsub_v1
from src.lib.task import CarbonAwareTask
from json import loads
import os
from zoneinfo import ZoneInfo
from datetime import datetime

PROJECT_ID =  os.environ["GCP_PROJECT_ID"]
SUBSCRIPTION_ID = os.environ["CARBON_AWARE_PUBSUB_SUBSCRIPTION"]

def read_new_carbon_aware_tasks() -> list[CarbonAwareTask]:
    """Reads new CarbonAwareTasks from a Pub/Sub subscription."""
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

    NUM_MESSAGES = 100
    new_tasks = []
    with subscriber:
        response = subscriber.pull(
            request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
        )

        if len(response.received_messages) == 0:
            return []

        ack_ids = []
        for received_message in response.received_messages:
            new_tasks.append(CarbonAwareTask(**loads(received_message.message.data), ingestion_time=datetime.fromtimestamp(received_message.message.publish_time.timestamp())))
            ack_ids.append(received_message.ack_id)

        # Acknowledges the received messages so they will not be sent again.
        subscriber.acknowledge(
            request={"subscription": subscription_path, "ack_ids": ack_ids}
        )

        print(
            f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
        )
        return new_tasks