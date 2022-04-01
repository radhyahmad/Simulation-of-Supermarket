class Product():
    all_items = [
            {
                'item': 'Susu',
                'harga': 50000,
                'code': '1'                  
                },
            {
                'item': 'daging',
                'harga': 20000,
                'code': '2'
                },
            {
                'item': 'lampu',
                'harga':15000,
                'code':'3'
                },
            {
                'item': 'masker',
                'harga': 25000,
                'code' : '4'
            },
            {
                'item': 'apel',
                'harga': 30000,
                'code': '5'
            }
        ]

    promotional_items = [
        {
            'item': 'Susu',
            'harga': 50000,
            'code': '1'
        },
        {
            'item':'masker',
            'harga': 25000,
            'code' : '2'
        }
    ]   
        
    def __init__(self,item,harga,code):
        self.item = item
        self.harga = harga
        self.code = code

    def display_product(self):
        print(self)
       
    def display_product_list(self):
        print("Our stockss")

    def check_product_on_all_items(self):
        found = False       
        for index, product in enumerate(self.all_items):
            #print(product)
                        
            if self.code == product['code']:                
                product_found = {'item': product['item'],'harga': product['harga'],'code': product['code']}
                found = True
                print(product['item']," -  Rp"+str(product['harga']),'\n' )
                
                
        if found == True :            
            return product_found
        else:
            return False
         
    
    def check_product_on_promotional_items(self):
        found = False       
        for index, product in enumerate(self.promotional_items):
            #print(product)
                        
            if self.code == product['code']:                
                product_found = {'item': product['item'],'harga': product['harga'],'code': product['code']}
                found = True
                print(product['item']," -  Rp"+str(product['harga']),'\n' )
                
                
        if found == True :            
            return product_found
        else:
            return False

    def set_bar_code(self,code):
        self.code = code

    def set_price(self,harga):
        self.haraga = harga   

   
        
        
