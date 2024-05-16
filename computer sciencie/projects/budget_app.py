class Category:
    def __init__(self, budget):
        self.budget = budget
        self.ledger=[]
        
        print(self.budget.center(30,"*"))
    
    def deposit(self, amount, description=''):
        
        deposit = {
            "amount":amount,
            "description": description
        }
        self.ledger.append(deposit)
        return True

    def withdraw(self, amount, description=''):
        self.amount=amount
        if self.check_fund():
            withdraw = {
                "amount": -amount,
                "description": description
            }
            self.ledger.append(withdraw)
            return True
        else:
            return False
    
    def get_balance(self):
        self.balance = 0
        for amount in self.ledger:
            self.balance += amount['amount']
        return self.balance
    
    def transfer(self, amount, destination):
        ledger=[]
        self.amount = amount
        
        if self.check_fund():
            self.withdraw(amount, f'Transfer from {Category.__class__.__name__}')
            self.deposit(amount, f'Transfer to {destination}')
            return True
        else:
            return False
            
    def check_fund(self):
        
        if self.get_balance() > self.amount:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        text =''
        for trans in self.ledger:
            desc=trans['description']
            amount = trans['amount']
            length = len(desc) + len(trans['description']) 
            if (len(desc) + len(trans['description']) )> 30:
                desc = trans['description'][:29-len(str(amount))]
                text += str(desc) + str(amount) + '\n'
            else:
                text += str(desc) + " "*(35-length)+ str(amount) + '\n'
        return text
    
def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

