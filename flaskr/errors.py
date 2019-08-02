class Error(Exception):
    pass

class InvalidAirportError(Error):

    def __init__(self, airport_id):
        self.airport_id = airport_id

class InvalidOriginError(InvalidAirportError):

    def __init__(self, airport_id):
        InvalidAirportError.__init__(self, airport_id)

    def error_message(self):
        return  '{} is not a valid origin'.format(self.airport_id)

class InvalidDestinationError(InvalidAirportError):

    def __init__(self, airport_id):
        InvalidAirportError.__init__(self, airport_id)

    def error_message(self):
        return '{} is not a valid destination'.format(self.airport_id)
