
from data_storage import products, next_product_id

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)
        self.product_detail = {"Name": self.name, "Category": self.category, "Price": self.price, "Qty": self.stock_quantity}
    def __str__(self):
        return f"{self.product_detail}"
           
class ProductManager:
    def add_product(self, name, category, price, stock_quantity):
        global next_product_id
        product = Product(next_product_id, name, category, price, stock_quantity)
        products[next_product_id] = product.product_detail
        next_product_id += 1
        return "\nProduct added successfully."

    def update_product(self, product_id, name, category, price, stock_quantity):
        if product_id in products:
            products[product_id]["Name"] = name
            products[product_id]["Category"] = category
            products[product_id]["Price"] = price
            products[product_id]["Qty"] = stock_quantity
            
            return "\nProduct updated successfully."
        else:
            return "\nProduct not found."

    def delete_product(self, product_id):
        if product_id in products:
            del products[product_id]
            
            return "\nProduct deleted successfully"
        else:
            return "\nProduct not found."
    
    def list_products(self):
        return products 
    
    def search_by_name(self, product_name):
        product_list = []
        for product_id, product_info in products.items():
            if product_info["Name"] == product_name:
                
                product_details = ", ".join(f"{key}: {value}" for key, value in product_info.items())
                product_list.append(f"ID: {product_id}, {product_details}")
        return product_list
       
    def search_by_category(self, product_category):
        product_list = []
        for product_id, product_info in products.items():
            if product_info["Category"] == product_category:
                
                product_details = ", ".join(f"{key}: {value}" for key, value in product_info.items())
                product_list.append(f"ID: {product_id}, {product_details}")
        return product_list
       
    
    def low_stock(self):
        # Print products with Qty less than 50
        stock_detail = []
        for product_id, product_info in products.items():
            if int(product_info["Qty"]) < 50:
                
                product_details = ", ".join(f"{key}: {value}" for key, value in product_info.items())
                stock_detail.append(f"ID: {product_id}, {product_details}")
        return stock_detail
    
    def add_stock(self, id, add_quantity):
        if id in products:
            products[id]["Qty"] = products[id]["Qty"] + add_quantity
            return "\nStock added successfully."
        else:
            return "\nProduct not found."

    
    def sale_stock(self, id, sale_quantity):
        if id in products:
            if products[id]["Qty"] - sale_quantity < 0:
                return "\nIn-Sufficient Stock. Sale Denied !!!"
            else:
                products[id]["Qty"] = products[id]["Qty"] - sale_quantity
                return "\nSales successful......"
        else:
            return "\nProduct not found."
