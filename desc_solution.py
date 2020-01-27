class Value:
    def __init__(self):
        self.amount = None

    def __set__(self, obj, value):
        if obj.commission:
            self.amount = int(value - value * obj.commission)

    def __get__(self, obj, obj_type):
        return self.amount
