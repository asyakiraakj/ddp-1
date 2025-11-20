class MyValue:
    def __init__(self, val):
        self.val = val

    #method add perlu di-overload agar other_val bisa int, bisa juga MyValue
    def __add__(self, other_val):
        if isintstance(self, other_val):
            return MyValue(self.val + other_val)
        return MyValue(other_val + self.val)