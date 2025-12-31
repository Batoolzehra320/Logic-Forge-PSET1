
class Teamwork:
    def __init__(self,contributions):
        self.contributions=contributions
        self.impact=[]
    def impact_calculation(self):
        n=len(self.contributions)
        self.impact=[1]*n
        self.left=1
        for i in range(n):
            self.impact[i]=self.left
            self.left*=self.contributions[i]
        self.right=1
        for i in range(n-1,-1,-1):
            self.impact[i]*=self.right
            self.right*=self.contributions[i]
        return self.impact
t=Teamwork([1,2,3,4])
print(t.impact_calculation())
