class Sample:

    def __init__(self):
        self.num = None
        self.mul = None

    def print_sample_obj(self, num, mul):
        self.num = num
        self.mul = mul


sample = Sample()
sample.print_sample_obj(12, 16)
sample.num = 13
sample1 = Sample()
sample1.print_sample_obj(15, 89)
print(sample.mul, sample.num)
print(sample1.mul, sample1.num)
