class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("min() arg is an empty sequence")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("max() arg is an empty sequence")
        return max(self)

el = ExtendedList([3, 1, 4, 1, 5, 9])
print(el.min())
print(el.max())
