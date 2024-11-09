# Console based Inventory Management System developed by M. Saghir Abbasi
# admin password = admin123
# user password = user123


from user_management import UserManager
from product_management import ProductManager
# from stock_management import StockManager

usermanager = UserManager()
productmanager = ProductManager()
# stockmanager = StockManager()

def admin_dashboard():
    while True:
        print("Admin Dashboard")
        print("1. List Products")
        print("2. Add Products")
        print("3. Update Products")
        print("4. Delete Product")
        print("5. Log out")
        choice = input("Select your option (1 to 5): ")
        
        if choice == '1':
            list_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            main()
        else:
            print("Invalid choice, please try again.")

def user_dashboard():
    while True:
        print("\nUser Dashboard")
        print("1. List Products")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_products()
        elif choice == "2":
            main()
        else:
            print("Invalid choice, please try again.")

def stock_dashboard():
    while True:
        print("\nStock Dashboard")
        print("1. List All Products")
        print("2. Search Products By Name")
        print("3. Search Products By Category")
        print("4. Low Stock List")
        print("5. Add Stock")
        print("6. Sale Stock")
        print("7. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_products()
        if choice == "2":
            search_by_name()
        if choice == "3":
            search_by_category()                
        elif choice == "4":
            low_stock()
        elif choice == "5":
            add_stock()
        elif choice == "6":
            sale_stock()
        elif choice == "7":
            print("Logging out...")
            main()
        else:
            print("Invalid choice, please try again.")
    
def list_products():
    print("\nList of Products:")
    products = productmanager.list_products()
    if products:
        for product_id, product_info in products.items():
            product_details = ", ".join(f"{key}: {value}" for key, value in product_info.items())
            print(f"ID: {product_id}, {product_details}")
    else:
        print("\nNo product found.")

def search_by_name():
    name = input("Enter Name of Product to Search: ")
    list_products = productmanager.search_by_name(name)
    if list_products:
        print(f"\nFound {len(list_products)} matching product(s) with the name '{name}':")
        for product in list_products:
            print(product)

def search_by_category():
    category = input("Enter Category of Products to Search: ")
    list_products = productmanager.search_by_category(category)
    if list_products:
        print(f"\nFound {len(list_products)} matching product(s) in category '{category}':")
        for product in list_products:
            print(product)
    
def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = input("Enter product price: ")
    stock_quantity = input("Enter product quantity: ") 
    message = productmanager.add_product(name, category, price, stock_quantity)
    print(message)

def update_product():
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = input("Enter product price: ")
    stock_quantity = input("Enter product quantity: ") 
    message = productmanager.update_product(product_id, name, category, price, stock_quantity)
    print(message)

def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    message = productmanager.delete_product(product_id)
    print(message)

def low_stock():
    low_products = productmanager.low_stock()
    if low_products:
        print("ATTENTION! LOW STOCK PRODUCTS")
    for low_product in low_products:
        print (low_product)
        
def add_stock():
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter quantity to add: "))
    message = productmanager.add_stock(product_id, quantity)
    print(message)
    
def sale_stock():
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Sales quantity: "))
    message = productmanager.sale_stock(product_id, quantity)
    print(message)
    
def admin_login():
    username = "admin"
    try:
        password = input("Enter Admin Password: ")
        current_user = usermanager.login(username, password)
        if current_user:
            print(f"Welcome {current_user.username}")
            admin_dashboard()
        else:
            print("\nInvalid login credentials!")
            main()
    except AttributeError:
        print("An error occurred: Unable to access user information.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def user_login():
    username = "user"
    try:
        password = input("Enter User Password: ")
        current_user = usermanager.login(username, password)
        if current_user:
            print(f"Welcome {current_user.username}")
            user_dashboard()
        else:
            print("\nInvalid login credentials")
            main()
    except AttributeError:
        print("An error occurred: Unable to access user information.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
            
def main():
    print("\nWelcome to Inventory Management System")
    print("Select User Option?")
    print("1. Admin")
    print("2. User")
    print("3. Stocks")
    print("4. Exit")
    choice = input("Select your option 1 to 3: ")
    if choice == '1':
        admin_login()
    elif choice == '2':
        user_login()
    elif choice == '3':
        stock_dashboard()
    elif choice == '4':
        exit()
    else:
        print("Invalid option...")
        
if __name__ == '__main__':
    main()