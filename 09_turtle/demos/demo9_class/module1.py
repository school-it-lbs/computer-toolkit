def sayMyName():
    print("module1")


class PrintLater:
    def __init__(self, n):
        self.n = n
    
    def doThePrint(self):
        print(self.n)
