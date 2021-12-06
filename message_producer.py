import time

from message_queue import MessageQueue
from message import APIMessage


class MessageProducer:
    """
    Send outbound messages.
    """

    def __init__(self, queue: MessageQueue):
        self.queue = queue

    def send20(self) -> None:
        """Send 20 messages in 1 second intervals."""
        for i in range(20):
            msg = APIMessage(str(i))
            self.queue.put(msg.convert())
            print(f"(Producer) put {msg.convert()}")
            time.sleep(1)
