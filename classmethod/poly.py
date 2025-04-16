class Math:
    def add(self, a, b, c=0,*args):
        print(args)  # Default parameter
        return a + b + c
    def sumNum(self, a, b, c=0,*args):
        print(args)  # Default parameter
        return a + b + c

m = Math()
print(m.add(5, 10,))      # Output: 15
print(m.add(5, 10, 20,12,34))  # Output: 35
print(m.sumNum(5, 10,))      # Output: 15
print(m.sumNum(5, 10, 20,12,34))  # Output: 35

