import sqlite3
import random
from datetime import datetime, timedelta

# Step 1: Create SQLite database
db_path = "my_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 2: Create Tables
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT UNIQUE,
        City TEXT
    );

    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        CategoryID INTEGER,
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    );

    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        OrderDate TEXT,
        TotalAmount REAL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    );

    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );

    CREATE TABLE IF NOT EXISTS Payments (
        PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        PaymentDate TEXT,
        Amount REAL,
        PaymentMethod TEXT,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    );

    CREATE TABLE IF NOT EXISTS Shippers (
        ShipperID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Phone TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        ProductID INTEGER,
        Rating INTEGER CHECK (Rating BETWEEN 1 AND 5),
        Comment TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );
""")

# Step 3: Insert Sample Data
# Generate 70 Customers
customer_names = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "David Lee", "Emma Wilson",
    "Frank White", "Grace Hall", "Hannah Scott", "Ian Taylor", "Jackie Moore"
] + [f"Customer_{i}" for i in range(11, 71)]

customer_cities = ["New York", "Los Angeles", "Chicago", "San Francisco", "Seattle", "Boston", "Denver", "Austin", "Miami", "Dallas"]
customer_data = [(name, f"{name.split()[0].lower()}@example.com", random.choice(customer_cities)) for name in customer_names]

cursor.executemany("INSERT OR IGNORE INTO Customers (Name, Email, City) VALUES (?, ?, ?)", customer_data)

# Generate 10 Product Categories
category_names = ["Electronics", "Appliances", "Furniture", "Clothing", "Books", "Toys", "Gaming", "Fitness", "Beauty", "Groceries"]
cursor.executemany("INSERT OR IGNORE INTO Categories (CategoryName) VALUES (?)", [(cat,) for cat in category_names])

# Generate 70 Products (Each belongs to a category)
product_names = [f"Product_{i}" for i in range(1, 71)]
product_prices = [random.uniform(50, 2000) for _ in range(70)]
product_categories = [random.randint(1, 10) for _ in range(70)]

product_data = list(zip(product_names, product_prices, product_categories))
cursor.executemany("INSERT OR IGNORE INTO Products (Name, Price, CategoryID) VALUES (?, ?, ?)", product_data)

# Generate 70 Orders
start_date = datetime(2024, 1, 1)
order_dates = [(start_date + timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d") for _ in range(70)]
order_customers = [random.randint(1, 70) for _ in range(70)]
order_amounts = [random.uniform(100, 5000) for _ in range(70)]

order_data = list(zip(order_customers, order_dates, order_amounts))
cursor.executemany("INSERT OR IGNORE INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)", order_data)

# Generate 70 Order Details
order_detail_data = [(random.randint(1, 70), random.randint(1, 70), random.randint(1, 5)) for _ in range(70)]
cursor.executemany("INSERT OR IGNORE INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (?, ?, ?)", order_detail_data)

# Generate 70 Payments
payment_methods = ["Credit Card", "Debit Card", "PayPal", "Google Pay", "Apple Pay", "UPI", "Cash"]
payment_dates = [(start_date + timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d") for _ in range(70)]
payment_data = [(random.randint(1, 70), payment_dates[i], order_amounts[i], random.choice(payment_methods)) for i in range(70)]
cursor.executemany("INSERT OR IGNORE INTO Payments (OrderID, PaymentDate, Amount, PaymentMethod) VALUES (?, ?, ?, ?)", payment_data)

# Generate 70 Shippers
shipper_names = [f"Shipper_{i}" for i in range(1, 71)]
shipper_phones = [f"98765{i:04d}" for i in range(1, 71)]
shipper_data = list(zip(shipper_names, shipper_phones))
cursor.executemany("INSERT OR IGNORE INTO Shippers (Name, Phone) VALUES (?, ?)", shipper_data)

# Generate 70 Reviews
review_comments = ["Great product!", "Not satisfied.", "Value for money.", "Would buy again.", "Poor quality."]
review_data = [(random.randint(1, 70), random.randint(1, 70), random.randint(1, 5), random.choice(review_comments)) for _ in range(70)]
cursor.executemany("INSERT OR IGNORE INTO Reviews (CustomerID, ProductID, Rating, Comment) VALUES (?, ?, ?, ?)", review_data)

# Step 4: Verify that tables were created
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("✅ Database setup completed successfully.")
print("📌 Tables in the database:", tables)

# Close connection
conn.commit()
conn.close()
