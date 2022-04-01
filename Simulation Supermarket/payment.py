class Payment():
    def __init__(self,checkout_items):
        self.checkout_items = checkout_items

    def add_item_to_cart(self,p):
        self.checkout_items.append(p)
        
    def display_checkout_items(self):
        print("Checkout Items")
        print(self.checkout_items)

    def calculate_payment_due(self):
        cart_items = self.checkout_items
        cart_totals = 0
        for index, product in enumerate(self.checkout_items):
            cart_totals += product['harga']
        self.due = cart_totals
        return cart_totals

    def pay_money(self,total):
        amount_to_pay = total
        print("\nPayment due: Rp"+str(amount_to_pay))
        change = self.accept_payment(amount_to_pay)
        return change
        
    def accept_payment(self, amount_to_pay):
        paid = float(0.0)
        customer_pay = float(0.0)
        due = float(0.0)
        total = amount_to_pay
        due = True
        
        while due == True:
            try:
                paid = float(input("\nPlease enter an amount to pay: "))
                if(paid < 0.0):
                    print("We don't accept negative money!\n")
                    continue
                else:
                    customer_pay += paid
                    self.customer_pay = customer_pay
                    if(paid < total):
                        due = total - paid
                        total = due
                        print("Payment due: Rp"+str(due))
                        due = True
                        continue   
                    else:
                        change = paid - total
                        self.change = change
                        return change
                    break
                break
                    
                    
            except ValueError:
                print('Please enter a valid floating point value.')
        return change
                        
    def print_receipt(self,change):
        print("\n----- Detail Receipt -----\n")

        for index, item in enumerate(self.checkout_items):
            print(item['item'],'     Rp'+str(item['harga']))

        print("\n")
        print("Total amount payment:",'     Rp'+str(self.due))
        


    
        
        
        
        
        
                        
                        
                

        
            
            
        
        
   
