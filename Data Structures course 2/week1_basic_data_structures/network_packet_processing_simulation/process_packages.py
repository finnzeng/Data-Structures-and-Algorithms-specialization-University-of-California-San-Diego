# python3


class Buffer:

    def __init__(self, size):
        self.size = size
        self.end_time = []

    def delete_processed(self, request):
        """deletes processed elements of the buffer by the request's arrival time."""
        while self.end_time:
            if self.end_time[0] <= request.arrival_time:
                self.end_time.pop(0)
            else:
                break

    def process(self, request):
        """Processes incoming request."""
        self.delete_processed(request)

        if len(self.end_time) == self.size: #if buffer is full
            return Response(True, -1)

        if len(self.end_time) == 0:   #if buffer is empty
            self.end_time = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)

        response = Response(False, self.end_time[-1])
        self.end_time.append(self.end_time[-1] + request.process_time)
        return response


class Request:
    """Incoming network packet."""

    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    """Response of the network buffer."""

    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def process_requests(requests, buffer):
    return [buffer.process(r) for r in requests]


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count)
    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)