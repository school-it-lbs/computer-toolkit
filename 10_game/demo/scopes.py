v = 'a'

print(f"1: {v}")

def example1():
    v = 'b'
    print(f"2: {v}")

example1()

print(f"3: {v}")

def example2(v):
    print(f"4: {v}")
    v = 'c'
    print(f"5: {v}")

example2(v)

print(f"6: {v}")


class ClassExample:
    def __init__(self, name, v):
        self.name = name
        self.v = v        
        
    def print_v(self):
        print(f"{self.name}: {self.v}")
        
        
c1 = ClassExample("Class 1", v)
v = 'd'
c2 = ClassExample("Class 2", v)

c1.print_v()
c2.print_v()
