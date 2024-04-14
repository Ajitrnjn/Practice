class WithPrivateAttribute:

    def __init__(self):
        self.__k = 9

    def _get_k(self):
        return self.__k


obj = WithPrivateAttribute()
print(obj._get_k())