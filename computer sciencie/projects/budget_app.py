class Category:
    def __init__(self, budget):
        self.budget = budget
        self.ledger=[]
        self.balance=0
        self.amount=0
        self.get_balance()

    
    def deposit(self, amount, description=''):
        
        deposit = {
            "amount":float(amount),
            "description": description
        }
        self.ledger.append(deposit)
        return True

    def withdraw(self, amount, description=''):
        if self.check_funds(float(amount)):
            withdraw = {
                "amount": -float(amount),
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
        if self.check_funds(float(amount)):
            self.withdraw(amount, f'Transfer to {destination.budget}')
            destination.deposit(amount, f'Transfer from {self.budget}')
            self.get_balance()
            return True
        
        else:
            return False
    
            
    def check_funds(self, amount):
        
        if self.get_balance() < amount:
            return False
        else:
            return True
    
    def __str__(self) -> str:
        self.get_balance()
        text =''
        text+=self.budget.center(30,"*")+'\n'
        ch_total = 30
        for trans in self.ledger:
            desc=trans['description']
            amount ='%.2f'%trans['amount']
            print(amount)
            length = len(desc) + len(str(amount))
            
            if (len(desc) + len(str(amount)) )> 30:
                desc = trans['description'][:29-len(str(amount))]
                text += desc + " " +str(amount) + '\n'
                continue
            text += desc + " "*(ch_total-length)+ amount + '\n'
        text += "Total: " + '%.2f'%self.balance
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


