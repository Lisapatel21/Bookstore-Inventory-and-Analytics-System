import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

DEFAULT_INVENTORY_CSV = """Title,Author,Genre,Price,Quantity
The Great Gatsby,F. Scott Fitzgerald,Fiction,10.99,25
To Kill a Mockingbird,Harper Lee,Fiction,12.50,18
1984,George Orwell,Dystopian,14.20,30
A Brief History of Time,Stephen Hawking,Science,18.00,12
Sapiens,Yuval Noah Harari,History,16.50,20
"""

DEFAULT_SALES_CSV = """Date,Title,Quantity Sold,Total Revenue
2026-01-10,1984,2,28.40
2026-01-15,The Great Gatsby,5,54.95
2026-02-01,Sapiens,3,49.50
2026-02-14,To Kill a Mockingbird,4,50.00
2026-03-05,A Brief History of Time,2,36.00
2026-03-12,1984,3,42.60
"""


def initialize_csv_files():
    """Generates default CSV files if they do not exist."""
    if not os.path.exists("inventory.csv"):
        with open("inventory.csv", "w", encoding="utf-8") as f:
            f.write(DEFAULT_INVENTORY_CSV)
        print("Created default 'inventory.csv' file.")

    if not os.path.exists("sales.csv"):
        with open("sales.csv", "w", encoding="utf-8") as f:
            f.write(DEFAULT_SALES_CSV)
        print("Created default 'sales.csv' file.")


class Book:

    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Genre": self.genre,
            "Price": self.price,
            "Quantity": self.quantity,
        }


class Bookstore:

    def __init__(
        self, inventory_file="inventory.csv", sales_file="sales.csv"
    ):
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.inventory = []
        self.load_inventory_data()

    def load_inventory_data(self):
        self.inventory = []
        if os.path.exists(self.inventory_file):
            df_inv = pd.read_csv(self.inventory_file)
            for _, row in df_inv.iterrows():
                book = Book(
                    row["Title"],
                    row["Author"],
                    row["Genre"],
                    row["Price"],
                    row["Quantity"],
                )
                self.inventory.append(book)

    def save_inventory(self):
        data = [b.to_dict() for b in self.inventory]
        df = pd.DataFrame(data)
        df.to_csv(self.inventory_file, index=False)

    def add_book(self, title, author, genre, price, quantity):
        if price <= 0 or quantity <= 0:
            print("Error: Price and Quantity must be positive values!")
            return False

        for book in self.inventory:
            if book.title.lower() == title.lower():
                book.quantity += quantity
                book.price = price
                self.save_inventory()
                print(f"Updated quantity for existing book: {title}")
                return True

        new_book = Book(title, author, genre, price, quantity)
        self.inventory.append(new_book)
        self.save_inventory()
        print(f"Book '{title}' added successfully!")
        return True

    def update_inventory(self, title, new_quantity):
        if new_quantity < 0:
            print("Error: Quantity cannot be negative!")
            return False

        found = False
        for book in self.inventory:
            if book.title.lower() == title.lower():
                book.quantity = new_quantity
                found = True
                break

        if found:
            self.save_inventory()
            print(f"Updated stock for '{title}' to {new_quantity}.")
        else:
            print(f"Book '{title}' not found in inventory.")
        return found

    def record_sale(self, title, quantity_sold, date_str):
        if quantity_sold <= 0:
            print("Error: Quantity sold must be greater than zero!")
            return False

        book_found = None
        for book in self.inventory:
            if book.title.lower() == title.lower():
                book_found = book
                break

        if not book_found:
            print(f"Error: Book '{title}' not found in inventory!")
            return False

        if book_found.quantity < quantity_sold:
            print(
                f"Error: Not enough stock! Available quantity is {book_found.quantity}."
            )
            return False

        book_found.quantity -= quantity_sold
        self.save_inventory()

        total_revenue = quantity_sold * book_found.price
        new_sale = pd.DataFrame(
            [
                {
                    "Date": date_str,
                    "Title": book_found.title,
                    "Quantity Sold": quantity_sold,
                    "Total Revenue": total_revenue,
                }
            ]
        )

        if os.path.exists(self.sales_file):
            new_sale.to_csv(self.sales_file, mode="a", header=False, index=False)
        else:
            new_sale.to_csv(self.sales_file, mode="w", header=True, index=False)

        print(
            f"Sale recorded successfully! Total Revenue generated: ${total_revenue:.2f}"
        )
        return True

    def generate_report(self):
        print("\n" + "=" * 55)
        print("         BOOKSTORE INVENTORY REPORT         ")
        print("=" * 55)

        if not self.inventory:
            print("No books available in inventory.")
            return

        total_items = sum(b.quantity for b in self.inventory)
        total_val = sum(b.price * b.quantity for b in self.inventory)

        print(f"{'Title':<25} | {'Genre':<12} | {'Price':<7} | {'Stock':<5}")
        print("-" * 55)
        for b in self.inventory:
            print(
                f"{b.title[:24]:<25} | {b.genre[:11]:<12} | ${b.price:<6.2f} | {b.quantity:<5}"
            )

        print("-" * 55)
        print(f"Total Unique Titles : {len(self.inventory)}")
        print(f"Total Books In Stock: {total_items}")
        print(f"Total Inventory Value: ${total_val:.2f}")
        print("=" * 55 + "\n")


class AnalyticsEngine:

    def __init__(
        self, inventory_file="inventory.csv", sales_file="sales.csv"
    ):
        self.inventory_file = inventory_file
        self.sales_file = sales_file

    def numpy_analysis(self):
        print("\n--- NUMPY NUMERICAL ANALYSIS ---")

        if not os.path.exists(self.inventory_file):
            print("Inventory file not found.")
            return

        df_inv = pd.read_csv(self.inventory_file)
        prices = df_inv["Price"].to_numpy()
        quantities = df_inv["Quantity"].to_numpy()

        if len(prices) == 0:
            print("No data to analyze.")
            return

        avg_price = np.mean(prices)
        median_price = np.median(prices)
        std_price = np.std(prices)
        total_stock_value = np.sum(prices * quantities)

        print(f"Average Book Price: ${avg_price:.2f}")
        print(f"Median Book Price:  ${median_price:.2f}")
        print(f"Price Std Deviation: ${std_price:.2f}")
        print(f"Total Valuation:    ${total_stock_value:.2f}")

        if os.path.exists(self.sales_file):
            df_sales = pd.read_csv(self.sales_file)
            if not df_sales.empty:
                df_sales["Date"] = pd.to_datetime(df_sales["Date"])
                daily_sales = (
                    df_sales.groupby("Date")["Total Revenue"].sum().values
                )
                if len(daily_sales) > 1:
                    growth_rates = np.diff(daily_sales) / daily_sales[:-1] * 100
                    print(
                        f"Average Daily Sales Growth Rate: {np.mean(growth_rates):.2f}%"
                    )

    def pandas_analysis(self):
        print("\n--- PANDAS SALES & INVENTORY ANALYSIS ---")

        if not os.path.exists(self.sales_file) or not os.path.exists(
            self.inventory_file
        ):
            print("Missing datasets for full Pandas analysis.")
            return

        df_inv = pd.read_csv(self.inventory_file)
        df_sales = pd.read_csv(self.sales_file)

        df_inv.dropna(inplace=True)
        df_sales.dropna(inplace=True)

        df_merged = pd.merge(df_sales, df_inv, on="Title", how="left")

        best_sellers = (
            df_merged.groupby("Title")["Quantity Sold"].sum().reset_index()
        )
        best_sellers = best_sellers.sort_values(
            by="Quantity Sold", ascending=False
        )

        print("\nTop 3 Selling Books:")
        print(best_sellers.head(3).to_string(index=False))

        if "Genre" in df_merged.columns:
            genre_revenue = (
                df_merged.groupby("Genre")["Total Revenue"].sum().reset_index()
            )
            print("\nRevenue by Genre:")
            print(genre_revenue.to_string(index=False))

    def create_visualizations(self):
        if not os.path.exists(self.sales_file) or not os.path.exists(
            self.inventory_file
        ):
            print("Cannot generate visualizations. Dataset files missing.")
            return

        df_inv = pd.read_csv(self.inventory_file)
        df_sales = pd.read_csv(self.sales_file)
        df_merged = pd.merge(df_sales, df_inv, on="Title", how="left")

        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(
            "Bookstore Analytics & Performance Dashboard",
            fontsize=16,
            fontweight="bold",
        )

        if "Genre" in df_merged.columns:
            genre_data = (
                df_merged.groupby("Genre")["Quantity Sold"].sum().reset_index()
            )
            sns.barplot(
                data=genre_data,
                x="Genre",
                y="Quantity Sold",
                hue="Genre",
                legend=False,
                ax=axes[0, 0],
                palette="viridis",
            )
            axes[0, 0].set_title("Total Quantity Sold by Genre")
            axes[0, 0].set_xlabel("Genre")
            axes[0, 0].set_ylabel("Units Sold")

        df_sales["Date"] = pd.to_datetime(df_sales["Date"])
        df_sales["YearMonth"] = df_sales["Date"].dt.to_period("M").astype(str)
        monthly_sales = (
            df_sales.groupby("YearMonth")["Total Revenue"].sum().reset_index()
        )

        sns.lineplot(
            data=monthly_sales,
            x="YearMonth",
            y="Total Revenue",
            marker="o",
            ax=axes[0, 1],
            color="b",
        )
        axes[0, 1].set_title("Monthly Revenue Trends")
        axes[0, 1].set_xlabel("Month")
        axes[0, 1].set_ylabel("Revenue ($)")
        axes[0, 1].tick_params(axis="x", rotation=45)

        if "Genre" in df_merged.columns:
            genre_rev = df_merged.groupby("Genre")["Total Revenue"].sum()
            axes[1, 0].pie(
                genre_rev.values,
                labels=genre_rev.index,
                autopct="%1.1f%%",
                startangle=140,
                colors=sns.color_palette("pastel"),
            )
            axes[1, 0].set_title("Revenue Share by Genre")

        corr_data = df_merged[["Price", "Quantity Sold", "Total Revenue"]].corr()
        sns.heatmap(
            corr_data, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1, 1]
        )
        axes[1, 1].set_title("Price vs Sales Volume Correlation")

        plt.tight_layout()
        plt.show()


def main():
    initialize_csv_files()

    store = Bookstore()
    analytics = AnalyticsEngine()

    while True:
        print("\n--- BOOKSTORE MANAGEMENT SYSTEM ---")
        print("1. View Inventory Report")
        print("2. Add New Book")
        print("3. Update Book Stock")
        print("4. Record a Sale")
        print("5. Run NumPy & Pandas Data Analysis")
        print("6. Show Analytics Visualizations")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            store.generate_report()

        elif choice == "2":
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            genre = input("Enter Genre: ").strip()
            try:
                raw_price = input("Enter Price: ").replace("$", "").strip()
                price = float(raw_price)
                qty = int(input("Enter Quantity: ").strip())
                store.add_book(title, author, genre, price, qty)
            except ValueError:
                print(
                    "Invalid input! Price must be numeric and Quantity must be an integer."
                )

        elif choice == "3":
            title = input("Enter Book Title to Update: ").strip()
            try:
                qty = int(input("Enter New Quantity: ").strip())
                store.update_inventory(title, qty)
            except ValueError:
                print("Invalid quantity! Must be an integer.")

        elif choice == "4":
            title = input("Enter Book Title Sold: ").strip()
            date_str = input("Enter Sale Date (YYYY-MM-DD): ").strip()
            try:
                qty = int(input("Enter Quantity Sold: ").strip())
                store.record_sale(title, qty, date_str)
            except ValueError:
                print("Invalid quantity format.")

        elif choice == "5":
            analytics.numpy_analysis()
            analytics.pandas_analysis()

        elif choice == "6":
            print("Rendering visual charts...")
            analytics.create_visualizations()

        elif choice == "7":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()