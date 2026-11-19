class Card:
    def __init__(self,value,kind):
        self.value = value
        self.kind = kind
        self.name = None
        if value == 11:
            self.name = "J"
        elif value == 12:
            self.name = "Q"
        elif value == 13:
            self.name == "k"
        elif value == 14:
            self.name = "A"
        else:
            self.name = None
        

    def __str__(self):
        if self.name is None:
            return f"{self.value}  {self.kind}"
        return f"{self.name} {self.kind}"
