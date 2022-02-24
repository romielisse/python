import csv
import sqlite3
from contextlib import closing

print("Customer Data Importer")
print()

# specify filenames in the current directory
csv_file = "customers.csv"
db_file = "customers.sqlite"
table_name = "Customer"

print("CSV file:   ", csv_file)
print("DB file:    ", db_file)
print("Table name: ", table_name)
print()

# connect to the database and set the row factory
conn = sqlite3.connect("customers.sqlite")
conn.row_factory = sqlite3.Row

# delete old rows in database
with closing(conn.cursor()) as c:
    sql =  '''DELETE FROM Customer'''
    c.execute(sql)
    conn.commit()
print(f"All old rows deleted from {table_name} table.")

# create SQL statement for inserting data into database
sql = '''INSERT INTO Customer
            (firstName, lastName, companyName, address, city, state, zip)
         VALUES
             (?, ?, ?, ?, ?, ?, ?)'''

# read customer data from file
with open(csv_file, "r", newline='') as infile:
    reader = csv.reader(infile)
    count = 0
    for row in reader:
        if count == 0:
            pass
        else:
            first =    row[0].strip()
            last =     row[1].strip()
            company =  row[2].strip()
            address =  row[3].strip()
            city =     row[4].strip()
            state =    row[5].strip()
            zip =      row[6].strip()
    
            # write the data to the database
            with closing(conn.cursor()) as c:            
                c.execute(sql, (first, last, company, address, city, state, zip))
        
        count += 1
        # print("Count:", count) # for debugging

conn.commit()
conn.close()

print(f"{count-1} row(s) inserted into Customer table.")
