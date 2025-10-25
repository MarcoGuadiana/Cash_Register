
class CashRegister:
    

    def __init__(self, discount=0):
        
        self._discount = 0
        self.discount = discount  
        self.total = 0.0
        self.items = []
        self.previous_transactions = []
        
  

    @property
    def discount(self):
       
        return self._discount

    @discount.setter
    def discount(self, value):
        
        if not isinstance(value, int):
            print("Not valid discount") 
            return

        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            return

    # Methods 

    def add_item(self, item, price, quantity=1):
        
        extended_price = price * quantity

       
        self.total += extended_price

        
        for _ in range(quantity):
            self.items.append(item)

       
        transaction = {
            "type": "item_added",
            "item_name": item,
            "quantity": quantity,
            "extended_price": extended_price
        }
        self.previous_transactions.append(transaction)
        
        

    def apply_discount(self):
        
        if self.discount == 0:
            
            print("There is no discount to apply.")
            return

        discount_rate = self.discount / 100
        discount_amount = self.total * discount_rate
        
        
        if self.total == 0.0:
             
             return 

        
        self.total -= discount_amount

        
        discount_transaction = {
            "type": "discount_applied",
            "percentage": self.discount,
            "amount_off": discount_amount
        }
        self.previous_transactions.append(discount_transaction)
        
        
        print(f"After the discount, the total comes to ${int(self.total)}.")


    def void_last_transaction(self):
        
        if not self.previous_transactions:
            
            print("There are no transactions to void.")
            return

       
        last_transaction = self.previous_transactions.pop()
        transaction_type = last_transaction["type"]

        if transaction_type == "item_added":
           
            item_name = last_transaction["item_name"]
            quantity = last_transaction["quantity"]
            extended_price = last_transaction["extended_price"]

           
            self.total -= extended_price

            
            for _ in range(quantity):
                
                if item_name in self.items:
                    self.items.remove(item_name) 

            

        elif transaction_type == "discount_applied":
           
            amount_off = last_transaction["amount_off"]
            self.total += amount_off
            