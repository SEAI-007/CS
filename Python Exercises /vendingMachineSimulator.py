class VendingMachine:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.internal_counter = 0

    def add_product(self,store_product_name, price, stock):
         self.internal_counter += 1
         store_id = self.internal_counter
         product = Product(store_id,store_product_name,price,stock, 0)
         self.products[store_id] = product

    def view_all_products(self):
        for product in self.products.values():
            print(product)

    def purchase_product(self, store_id):
        try:
            if self.products[store_id].stock > 0:
                self.products[store_id].stock -= 1
                self.products[store_id].sales += 1
                print("-----PURCHASED SUCCESFULLY-----")
        except:
            print("Please enter a valid product number")

    def restock_product(self, store_id, restock):
        self.products[store_id].stock += restock

    def show_statistics(self):
        total_products = len(self.products)
        total_sales = 0
        total_stock = 0
        for product in self.products:
            total_sales += product.sales
        for product in self.products:
            total_stock += product.stock
        print(f"Total Products: {total_products} , Total stock: {total_stock}, Total sales {total_sales}")


class Product:
    def __init__(self, store_id, name, price, stock, sales):
        self.store_id = store_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.sales = int(sales)

    def __str__(self):
        return f"{self.store_id, self.name, self.price, self.stock, self.sales}"

def menu_system():
    VendingMachine_1 = VendingMachine("SUPERDUPER VENDING MACHINE 3000")
    choice = ""
    while choice != "quit":
        print("""
              \n-------------------------
               \n1. Add Product
               \n2. View All Products
               \n3. Purchase Product
               \n4. Restock Product
               \n5. Show Statistics
               \n6. Exit
              \n-------------------------
        """)
        choice = input("What do you want to execute? ")
        try:
            if choice == "1": #add Products
                product_name = input("What is the name of the product? ")
                price = input("What is the price of the product? ")
                stock = input("What is the stock? ")
                VendingMachine_1.add_product(product_name, price, stock)
                print("-----ADDED SUCCESFULLY-----")
            elif choice == "2": #view Products
                VendingMachine_1.view_all_products()
            elif choice == "3": #purchase Product
                wanted_product = int(input("Please input the number of the product wanted. "))
                try: 
                    VendingMachine_1.purchase_product(wanted_product)
                except:
                    print("An error has appeared. ")
            elif choice == "4":
                wanted_restock = int(input("Please input the number of the product wanted to restock "))
                quantity = int(input("How much should be restocked? "))
                try:
                    VendingMachine_1.restock_product(wanted_restock, quantity)
                except:
                    print("An error has appeared")
            elif choice == "5":
                VendingMachine_1.show_statistics()
            elif choice == "6":
                choice = input("Do you wish to continue (y/n)? ")
                if choice == "y":
                    return True
                else:
                    pass
            else:
                print("Pick a valid number")
                return
        except:
            print("An error has occured")
            return

menu_system()