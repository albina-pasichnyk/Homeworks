class CustomIterator:
    """Class of Custom Iterator"""

    def __init__(self, input_sequence, start_index, end_index):
        self.sequence = input_sequence
        self.start_index = start_index
        self.end_index = end_index

    def __iter__(self):
        """Return iter(self)"""
        return self

    def __next__(self):
        """Next function of iterator with specific conditions"""
        if self.start_index > self.end_index:
            raise StopIteration
        processed_element = self.sequence[self.start_index]
        self.start_index += 1
        return processed_element


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5]
    custom_interator = CustomIterator(sequence, 2, 4)
    my_iterator = iter(custom_interator)
    for each in my_iterator:
        print(each)
