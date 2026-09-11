[README (10).md](https://github.com/user-attachments/files/32104973/README.10.md)
# Bookstore Inventory and Analytics System

## Description

This Python project manages a bookstore's inventory and analyzes sales data. It utilizes Object-Oriented Programming (OOP) principles, custom input validations, NumPy calculations, Pandas DataFrames, and Matplotlib/Seaborn visualization graphs.

## Features

- **Inventory Management**: Add, update stock levels, and store inventory records into `inventory.csv`.
- **Sales Record System**: Process orders, deduct inventory automatically, and store transaction details inside `sales.csv`.
- **NumPy Computation**: Computes mean prices, standard deviations, valuation, and sales growth rates.
- **Pandas Analysis**: Identifies top-selling titles and revenue distribution per category.
- **Data Visualizations**: Generates bar graphs, line charts, pie charts, and correlation heatmaps.

## Instructions to Run

1. Ensure `python3`, `pandas`, `numpy`, `matplotlib`, and `seaborn` are installed:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

2. Run the program:

   ```bash
   python bookstor_system.py
   ```

3. On first run, default `inventory.csv` and `sales.csv` files are created automatically if they don't already exist.

4. Use the on-screen menu to view reports, add books, update stock, record sales, run data analysis, and generate visualizations.

## Sample Program Output

Below is a walkthrough of the program running end-to-end: viewing the inventory report, adding a new book, updating stock, recording a sale, and running the NumPy/Pandas analysis.

### 1. Viewing the Inventory Report

```
--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 1

=======================================================
         BOOKSTORE INVENTORY REPORT
=======================================================
Title                     | Genre        | Price   | Stock
-------------------------------------------------------
The Great Gatsby          | Fiction      | $10.99  | 25
To Kill a Mockingbird     | Fiction      | $12.50  | 18
1984                      | Dystopian    | $14.20  | 30
A Brief History of Time   | Science      | $18.00  | 12
Sapiens                   | History      | $16.50  | 20
The Midnight Library      | Fantasy Fic  | $18.00  | 2
-------------------------------------------------------
Total Unique Titles : 6
Total Books In Stock: 107
Total Inventory Value: $1507.75
=======================================================
```

### 2. Adding a New Book and Updating Stock

```
--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 2
Enter Title: The Midnight Library
Enter Author: Matt Haig
Enter Genre: Fantasy Fiction
Enter Price: $18.00
Enter Quantity: 1
Updated quantity for existing book: The Midnight Library

--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 3
Enter Book Title to Update: The Midnight Library
Enter New Quantity: 10
Updated stock for 'The Midnight Library' to 10.
```

### 3. Recording a Sale and Running NumPy Analysis

```
--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 4
Enter Book Title Sold: The Midnight Library
Enter Sale Date (YYYY-MM-DD): 2024-09-21
Enter Quantity Sold: 6
Sale recorded successfully! Total Revenue generated: $108.00

--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 5

--- NUMPY NUMERICAL ANALYSIS ---
Average Book Price: $15.03
Median Book Price:  $15.35
Price Std Deviation: $2.68
Total Valuation:    $1543.75
Average Daily Sales Growth Rate: -0.42%
```

### 4. Pandas Analysis and Exiting the Program

```
--- PANDAS SALES & INVENTORY ANALYSIS ---

Top 3 Selling Books:
              Title  Quantity Sold
The Midnight Library              7
               1984              5
    The Great Gatsby              5

Revenue by Genre:
        Genre  Total Revenue
    Dystopian          71.00
Fantasy Fiction        126.00
      Fiction         104.95
      History          49.50
      Science          36.00

--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 6
Rendering visual charts...

--- BOOKSTORE MANAGEMENT SYSTEM ---
1. View Inventory Report
2. Add New Book
3. Update Book Stock
4. Record a Sale
5. Run NumPy & Pandas Data Analysis
6. Show Analytics Visualizations
7. Exit
Enter choice (1-7): 7
Exiting application. Goodbye!
```

## Data Visualizations

Running option **6. Show Analytics Visualizations** generates the following charts:

### Total Quantity Sold by Genre

A bar chart showing total units sold per genre. Fiction leads with 9 units sold, followed by Fantasy Fiction (7), Dystopian (5), History (3), and Science (2).

### Monthly Revenue Trends

A line chart tracking total revenue by month. Revenue peaked at $126 in September 2024, then settled between roughly $78 and $99 across January–March 2026.

### Revenue Share by Genre

A pie chart showing each genre's share of total revenue: Fantasy Fiction (32.5%), Fiction (27.1%), Dystopian (18.3%), History (12.8%), and Science (9.3%).

### Price vs Sales Volume Correlation

A heatmap of correlations between Price, Quantity Sold, and Total Revenue. Quantity Sold and Total Revenue are strongly correlated (0.91), while Price shows a weak negative correlation with Quantity Sold (-0.32) and almost no correlation with Total Revenue (0.08).

## Author

**Lisa Patel**
