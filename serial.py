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
        # start should never change
        self.start = start
        self.count = 0
        # can have self.next attribute/property
        self.next = self.start + self.count



    # don't forget to write a __repr__ for this class

    def generate(self):
        """When called, start number increase by 1."""
        # potential other way to write this
        if self.count == 0 :
            # print("currStartNum=", self.start)
            self.count += 1
            return self.next
        else :
            self.next += 1
            self.count += 1
            # print("nextStartNum=", self.start)
        return self.next

    def reset(self):
        """Function resets to intial start number."""
        self.next = self.next - self.count + 1
        self.count = 0
        return None






