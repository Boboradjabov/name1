class Class:
    def __init__(self,color,model,number):
        self.color=color
        self.model = model
        self.price=number
    def add_balance(self,money):
       self.price+=money
mers=Class('Black','Mersidec',10999)
print(mers.color,mers.model,mers.price)
