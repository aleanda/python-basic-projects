# Customer Orders Analysis

## Overview
This project performs a basic analysis of customer orders data using Python.  
The goal is to extract meaningful insights about customer behavior and category performance from a structured dataset.

---

## Objectives
- Compute total revenue generated from all orders
- Identify the customer with the highest total spending
- Determine the best-performing product category
- Aggregate data across multiple dimensions (customers and categories)

---

## Dataset
The dataset (`orders.csv`) contains the following fields:

- `order_id`: unique identifier of the order  
- `customer`: customer name  
- `category`: product category  
- `amount`: transaction value  

The dataset was pre-processed and cleaned using Excel before being analyzed in Python.

---

## Methodology
The analysis is performed using the built-in `csv` module in Python.

Key steps:
1. Load the dataset using `csv.DictReader`
2. Iterate through each row of the dataset
3. Convert numeric fields from string to float
4. Aggregate:
   - total revenue
   - customer-level spending
   - category-level revenue
5. Identify maximum values using dictionary-based aggregation

---

## Results
Example output:

Total revenue: 2940.0
Best customer: Alice
Best category: Electronics


---

## Technologies Used
- Python (standard library: `csv`)
- Excel (data cleaning and sorting)

---

## Project Structure
03_customer_analysis/
│
├── main.py
├── orders.csv
└── README.md


---

## Key Learnings
- Reading and processing structured data from CSV files
- Using dictionaries for data aggregation
- Performing simple analytical computations
- Translating raw data into actionable insights

---

## Future Improvements
- Use `pandas` for more efficient data manipulation
- Add data visualization (e.g. charts)
- Handle missing or inconsistent data
- Extend analysis with additional metrics (e.g. average order value)

---

## Author
This project is part of my learning path in data analysis, focusing on building practical skills with Python and real-world data.
