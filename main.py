import sqlite3

# file work
file = open("data.txt", "w")
file.write("Hello, World")
file.write("\nPython is awesome")
file.write("\nI love programming")

file.close()

file = open("data.txt", "r")
content_file = file.read()
print(content_file)

file.close()

#SQLite
#Table users
def create_users():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE users ( 
        id INT PRIMARY KEY,
        name TEXT,
        email TEXT        
    )""")
    conn.close()

def add_users():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    name = input("Введите name: ")
    email = input("Введите email: ")

    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')

    result = cursor.fetchall()
    print(result)
    conn.close()

try:
    create_users()
except:
    print("Уже существует")
    add_users()
    get_users()



#Table products
def create_products():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE products (
        id INT PRIMARY KEY,
        name TEXT,
        price FLOAT,
        quantity INT
    )""")
    conn.close()

def add_products():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    products = [
        (1, "Bread", 30.55, 60),
        (2, "Oil", 90.89, 85),
        (3, "Potato", 35.00, 70)
    ]

    for product in products:
        cursor.execute("INSERT INTO products (id, name, price, quantity)"
                       " VALUES (?, ?, ?, ?)", product)
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    result = cursor.fetchall()
    print(result)
    conn.close()

try:
    create_products()
except:
    print("Уже существует")
    add_products()
    get_products()
