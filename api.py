import datetime
import typing


class API:
    """
    A rate limited API which takes x requests every y seconds.
    """

    def __init__(self, x: int, y: float) -> None:
        self.x = x
        self.y = y
        self.requests_dict = {}

    def run(self, message: str) -> str:
        current_time = datetime.datetime.now().timestamp()
        requests_count = self._get_requests_from_window(current_time)

        if requests_count < self.x:
            self.requests_dict[current_time] = (
                self.requests_dict.get(current_time, 0) + 1
            )
            return True
        else:
            return False

    def _get_requests_from_window(self, current_time: float) -> int:
        """
        Get the number of requests made from user_id in the last y seconds.

        Delete entries older than y seconds.
        """
        start_time = current_time - self.y

        requests_count = 0
        for timestamp, count in list(self.requests_dict.items()):
            if timestamp > start_time:
                requests_count += count
            else:
                del self.requests_dict[timestamp]

        return requests_count


"""
Comments.

The implementation assumes a single-threaded environment. 
In a multi-threaded environment, we'll need to lock down the self.requests_dict add/delete/modify behaviour.

This also doesn't scale well if the rate-limit is large, i.e. hours or days. If that is the case,
we'll most likely need to create buckets of start_times.

This also doesn't scale because all the information is stored on one self.requests_dict instance.

The delete process should ideally have some buffer (z seconds) before start_time.

We can also implement a running algorithm to avoid re-computation.
"""
