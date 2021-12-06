import threading

from api import API
from message_consumer import MessageConsumer
from message_producer import MessageProducer
from message_queue import RateLimitedMessageQueue


if __name__ == "__main__":
    # Limitation 3 requests every 5 seconds
    msg_queue = RateLimitedMessageQueue(3, 5)

    # Setup message consumer and producer nodes
    msg_consumer = MessageConsumer(msg_queue)
    msg_producer = MessageProducer(msg_queue)

    # Setup API call
    api = API(3, 5)

    # Setup running threads
    consumer_thread = threading.Thread(
        target=msg_consumer.process, kwargs={"ttl": 100, "func": api.run}
    )
    producer_thread = threading.Thread(target=msg_producer.send20)

    # Start threads
    consumer_thread.start()
    producer_thread.start()
