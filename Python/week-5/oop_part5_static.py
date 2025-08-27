#final stretch in this video
#making a global function that can be called anywhere, put in classes for organization

class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def pr():
        print("run")
    
print(Math.add5(6))
Math.pr()