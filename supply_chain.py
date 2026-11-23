class SupplyChain:

    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name):
        if product_id in self.products:
            print("Product Already Exists!")
        else:
            self.products[product_id] = {
                "name": name,
                "status": "Manufactured",
                "history": ["Manufactured"]
            }
            print("Product Added Successfully!")

    def update_status(self, product_id, status):
        if product_id in self.products:
            self.products[product_id]["status"] = status
            self.products[product_id]["history"].append(status)
            print("Product Status Updated!")
        else:
            print("Product Not Found!")

    def track_product(self, product_id):
        if product_id in self.products:
            product = self.products[product_id]

            print("\nProduct Name:", product["name"])
            print("Current Status:", product["status"])
            print("Tracking History:")

            for step in product["history"]:
                print("->", step)
        else:
            print("Product Not Found!")

    def display_products(self):
        for product_id, product in self.products.items():
            print(product_id, product["name"], product["status"])


system = SupplyChain()

while True:
    print("\n--- SUPPLY CHAIN MANAGEMENT ---")
    print("1. Add Product")
    print("2. Update Product Status")
    print("3. Track Product")
    print("4. Display Products")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        system.add_product(product_id, name)

    elif choice == "2":
        product_id = input("Product ID: ")
        status = input("Enter Status: ")
        system.update_status(product_id, status)

    elif choice == "3":
        product_id = input("Product ID: ")
        system.track_product(product_id)

    elif choice == "4":
        system.display_products()

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")
