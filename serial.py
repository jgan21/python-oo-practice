class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial number starting at a given number(ie.100)."""
        self.start = start
        self.count = 0

    def generate(self):
        """When called, start number increase by 1."""
        if self.count == 0 :
            # print("currStartNum=", self.start)
            self.count += 1
            return self.start
        else :
            self.start += 1
            self.count += 1
            # print("nextStartNum=", self.start)
        return self.start

    def reset(self):
        """Function resets to intial start number."""
        self.start = self.start - self.count + 1
        self.count = 0
        return None






