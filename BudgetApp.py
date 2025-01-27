class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return self.get_balance() >= amount
    
    def __str__(self):
        title = f"*************{self.name}*************"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total


def create_spend_chart(categories):
    # Calculate total spent in each category
    total_spent = sum(sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories)
    
    # Create chart data with percentage spent
    chart_data = []
    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        percentage = (spent / total_spent) * 100 if total_spent > 0 else 0
        chart_data.append((category.name, int(percentage)))
    
    # Prepare the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for _, percentage in chart_data:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    # Prepare the category names vertically
    max_name_length = max(len(category.name) for category, _ in chart_data)
    for i in range(max_name_length):
        chart += "     "
        for category, _ in chart_data:
            chart += category[i] if i < len(category) else " "
            chart += "  "
        chart += "\n"
    
    return chart.strip()
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)