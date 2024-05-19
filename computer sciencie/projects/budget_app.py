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
            length = len(desc) + len(str(amount))
            
            if (len(desc) + len(str(amount)) )> 30:
                desc = trans['description'][:29-len(str(amount))]
                text += desc + " " +str(amount) + '\n'
                continue
            text += desc + " "*(ch_total-length)+ amount + '\n'
        text += "Total: " + '%.2f'%self.balance
        return text
    
def create_spend_chart(categories):
    count=0
    aux=0
    percentage = {}
    
    clasification, total_bills = cat_and_total_amount(categories)
    
    percentage = take_percentage(clasification, total_bills)
    
    string=draw_chart(percentage)
    
    if categories[-1]:
        string += "\n"+ " "*4 + '-'*(len(categories)*3+1)
    
    larger =  max(clasification.keys(), key=len)
    shorter = min(clasification.keys(), key=len)

    
    for lenght in range(len(larger)):
        string+='\n'
        for cat in clasification.keys():
            try:
                if cat == categories[0].budget:
                    if lenght >= len(larger)-len(shorter)-1:
                        
                        string += " "*6
                            
                        
                    else:
                        string += " "*5+cat[lenght] #+ "  "
                
               
                elif lenght == len(larger) and larger[lenght] == larger[-1]:
                    print(lenght, len(larger))
                    string += " "*2 + cat[lenght] + "  "
                 
                else:
                    string += " "*2+cat[lenght]
            except:
                
                string += " "*3
            
       # print(string)
        string += "  "
    return string
                
def cat_and_total_amount(categories):
    clasification = {}
    total_bills = 0
    for category in categories:
        
        for bill in category.ledger:
            if bill['amount'] < 0 and bill['description'][:8].lower() != 'transfer':
                total_bills += bill['amount']
                if category.budget in clasification:
                    aux = clasification[category.budget] + bill['amount']
                    clasification[category.budget] = aux
                    
                else:
                    clasification[category.budget] = bill['amount']
    
    return clasification, total_bills
    
def take_percentage(clasification, total_bills):
    percentage = {}
    for category in clasification.keys():
        percentage[category] = round(clasification[category] / total_bills * 100,1)
    
    return percentage


def draw_chart(percentage):
    keys = list(percentage.keys())
    string=''
    print(list(keys))
    try:
        string+='Percentage spent by category' + '\n'
        for col in range(100,-1,-10):
            if col >= 10 and col < 100:
                string += " " + str(col) + "|" + " "
            elif col < 10:
                string += "  " + str(col) + "|"+ " "
            else:
                string += "" + str(col) + "|"+ " "
            for key in keys:
                if percentage[key] >= col:
                    # if keys[-1]:
                    #     string +=  "o"
                    # else:
                    string +=  "o" + "  "
                else:
                    string +=  " "+ "  "
            if col != 0:
                string += '\n'
        return string
    except:
        pass
    