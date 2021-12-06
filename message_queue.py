import datetime
import queue
import typing

from message import Message


class MessageQueue:
    """
    A simple message queue.
    """

    def __init__(self):
        self.queue = queue.Queue()

    def put(self, message: Message) -> None:
        """Put a message in the queue."""
        self.queue.put(message)

    def get(self) -> Message:
        """Get a message from the queue."""
        return self.queue.get()


class RateLimitedMessageQueue(MessageQueue):
    """
    A rate limited message queue allowing x requests for every y seconds.
    """

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.prev_requests = queue.PriorityQueue(maxsize=self.x)

    def get(self) -> typing.Optional[Message]:
        """Get a message from the rate limited queue."""
        if self.queue.empty():
            return None

        current_time = datetime.datetime.now().timestamp()

        if not self.prev_requests.full():
            self.prev_requests.put(current_time)
            return self.queue.get()
        else:
            oldest_call = self.prev_requests.get()
            minimum_allowed = current_time - self.y
            if minimum_allowed > oldest_call:
                self.prev_requests.put(current_time)
                return self.queue.get()
            else:
                # Doing this because I don't think python PQ has a peek function
                self.prev_requests.put(oldest_call)
                return None
