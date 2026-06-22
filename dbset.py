
import psycopg2
print("working")
import pandas as pd
import pandas.io.sql as sqlio


conn = psycopg2.connect(database="python_course", user="postgres", password="example", host="localhost",port=5433)
cur = conn.cursor()

sql_create_table = """CREATE TABLE IF NOT EXISTS transactions(
            inv_id SERIAL PRIMARY KEY,
            InvoiceNo VARCHAR(255),
            StockCode VARCHAR(255),
            Description VARCHAR(255),
            Quantity real,
            InvoiceDate VARCHAR(255),
            UnitPrice real,
            CustomerID integer,
            Country VARCHAR(255)
        )"""

cur.execute(sql_create_table)

conn.commit()

cur.execute("""
INSERT INTO transactions (
    InvoiceNo, StockCode, Description,
    Quantity, InvoiceDate, UnitPrice,
    CustomerID, Country
)
VALUES
('536370','22492','MINI PAINT SET VINTAGE',36,'12/1/2010 8:45',0.65,12583,'France'),
('536371','22632','HAND WARMER RED POLKA DOT',6,'12/1/2010 9:01',1.85,17850,'United Kingdom'),
('536372','22745','POPPY DESIGN BOWL',12,'12/1/2010 9:15',2.10,17850,'United Kingdom')
""")

conn.commit()

query_invoice = """SELECT * FROM transactions where InvoiceNo = '536370'"""
cur.execute(query_invoice)

records = cur.fetchall()

print(records)

data = sqlio.read_sql(query_invoice, conn)
print(data)

cur.close()
conn.commit()


