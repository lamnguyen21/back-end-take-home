from bloom_filter import BloomFilter

'''
    AirportRepository uses a bloom filter to check if an airport code exists.
    Bloom filter best suits for this use case thanks to its minimum memory
    consumption given a large amount of data and its guarantee that false
    negative is impossible
'''
class AirportRepository(object):

    def __init__(self):
        self.bloom = BloomFilter()

    def add(self, airport_code):
        self.bloom.add(airport_code)

    def has(self, airport_code):
        return airport_code in self.bloom
