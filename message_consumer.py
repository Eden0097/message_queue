import datetime
import time
import typing

from message_queue import MessageQueue


class MessageConsumer:
    """
    Process messages in queue.
    """

    def __init__(self, queue: MessageQueue):
        self.queue = queue

    def process(self, ttl: int, func: typing.Callable) -> None:
        """Process queue'd messages for ttl seconds."""
        start_time = datetime.datetime.now().timestamp()
        end_time = start_time + ttl

        current_time = start_time
        while current_time < end_time:
            msg = self.queue.get()
            if msg is not None:
                response = func(msg)
                print(
                    f"(Consumer) time: {current_time - start_time} | msg: {msg} | response: {response}"
                )
            else:
                print(f"(Consumer) {current_time - start_time}")

            time.sleep(1)  # sleep to make logs more readable
            current_time = datetime.datetime.now().timestamp()
