from product import Product
from payment import Payment
#import sys
import os
import sys
wishlist = []

print("\n--------Welcome to Simuation of Supermarket!--------\n")
product_promo = Product('item','harga', 'code')
print('There are promotional items: ', product_promo.promotional_items)

def scan_product():
    code = int(input("\nPlease enter promotional items[1] or all items[2]: "))
    if code == 1:
        print('you choose promotional items!')
        scan_product_promotional_items()

    if code == 2:
        print('you choose all items!')
        scan_product_all_items()
    
def scan_product_promotional_items():
    code = input("\nPlease enter the code of your promotional items --> [1]susu, [2]masker: ")
    p1 = Product("","",code)
    search_product = p1.check_product_on_promotional_items()
    if(search_product == False):
        print("This product does not exist in our stocks.\n")
        scan_another_promotional_items()
    else:        
        wishlist.append(search_product)
        scan_another_promotional_items()
    
def scan_another_promotional_items():
    scan_another = input("Would you like to choose another promotional item products? (Y/N)")
    if(scan_another == 'y' or scan_another == 'Y'):
        scan_product_promotional_items()

def scan_product_all_items():
    code = input("\nPlease enter the code of your all items --> [1]susu, [2]daging, [3]lampu, [4]masker, [5]apel: ")
    p1 = Product("","",code)
    search_product = p1.check_product_on_all_items()
    if(search_product == False):
        print("This product does not exist in our stocks.\n")
        scan_another_all_items()
    else:        
        wishlist.append(search_product)
        scan_another_all_items()
    
def scan_another_all_items():
    scan_another = input("Would you like to choose another all item products? (Y/N)")
    if(scan_another == 'y' or scan_another == 'Y'):
        scan_product_all_items()

def main():
    scan_product()
    c1 = Payment(wishlist)
    total_payment = c1.calculate_payment_due()
    change = c1.pay_money(total_payment)
    #print("Change:",change)
    c1.print_receipt(change)
    print("\nThank you for shopping at Simulation of Supermarket!")

    next = input("(N)ext, or (Q)uit? ")
    if(next == "n" or next == "N"):
        wishlist[:] = []
        main()     
    else:
        #sys.exit(0)
        exit()

main()


    
