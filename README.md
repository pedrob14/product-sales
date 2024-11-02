### **1. Data Collection and Insertion (SQL)**

- Create a database and a table in SQL.
- Insert data into the table. Let's use a simple example of sales data:

```python
CREATE DATABASE Sales;
USE Sales;

CREATE TABLE Sales (
    ID INT PRIMARY KEY,
    Product VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2),
    Date DATE
);

INSERT INTO Sales (ID, Product, Quantity, Price, Date)
VALUES
(1, 'Product A', 10, 15.50, '2024-10-01'),
(2, 'Product B', 5, 25.00, '2024-10-02'),
(3, 'Product C', 8, 30.00, '2024-10-03');
```

### **2. Data Analysis and Manipulation (Python)**

- Use Python to connect to the SQL database and perform analysis. Here’s an example using pandas and sqlalchemy:


```python
import pandas as pd
from sqlalchemy import create_engine

# Connecting to the database
engine = create_engine('mysql+pymysql://username:password@localhost/Sales')

# Loading data from the sales table
df = pd.read_sql('SELECT * FROM Sales', engine)

# Analyzing the data
df['Total'] = df['Quantity'] * df['Price']
summary = df.groupby('Product').agg({'Quantity': 'sum', 'Total': 'sum'}).reset_index()

print(summary)
```

### **3. Data Visualization (Power BI)**

- Import the analyzed data into Power BI.
- Create a new dashboard and import the CSV file with the data analyzed in Python.
- Visualize the total quantity sold and total sales per product using bar charts.
