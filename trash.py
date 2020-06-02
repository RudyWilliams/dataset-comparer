class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reassign(self, new_a, new_b):
        a = self.a
        b = self.b

        a = new_a
        b = new_b

        self.a = a
        self.b = b
        return self


if __name__ == "__main__":
    s = Sample(5, 8)
    s.reassign(15, 28)
    print(s.a, s.b)
