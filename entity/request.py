from exeptions import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, req_str, storages):
        split_req = req_str.lower().split(' ')
        if len(split_req) != 7 or not split_req[1].isdigit():
            raise InvalidRequestError

        self.amount = int(split_req[1])
        self.product = split_req[2]
        self.departure = split_req[4]
        self.destination = split_req[6]

        if self.destination not in storages or self.departure not in storages:
            raise UnknownStorageError
