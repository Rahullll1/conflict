import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os
from config import DB_CONFIG  # Import DB_CONFIG

# Step 1: GUI to select an Excel (.xlsx) file
def get_excel_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Excel File with Stock Data",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    return file_path

# Step 2: Load Excel data using Pandas
def load_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

# Step 3: Clean and process data using Pandas and NumPy
def preprocess_data(df):
    df["Date"] = pd.to_datetime(df["Date"])
    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    df.dropna(inplace=True)
    df["Price_Change_Percent"] = ((df["Close"] - df["Open"]) / df["Open"]) * 100
    print("\nConverted DataFrame:\n", df.head())  # Show in terminal
    return df

# Step 4: Save data into MySQL using mysql.connector
def save_to_database(df):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # SQL Script to create the table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS StockData (
            Date DATE,
            Symbol VARCHAR(10),
            Open FLOAT,
            High FLOAT,
            Low FLOAT,
            Close FLOAT,
            Volume BIGINT,
            Price_Change_Percent FLOAT
        );
        """
        cursor.execute(create_table_sql)

        # Clear previous data
        cursor.execute("DELETE FROM StockData")

        # Insert new data
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO StockData (Date, Symbol, Open, High, Low, Close, Volume, Price_Change_Percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row["Date"].strftime('%Y-%m-%d'),
                row["Symbol"],
                row["Open"],
                row["High"],
                row["Low"],
                row["Close"],
                int(row["Volume"]),
                row["Price_Change_Percent"]
            ))

        conn.commit()
        print("Data saved to database successfully.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Step 5: Plot ups and downs for each symbol
def plot_stock_trends(df):
    if "Symbol" not in df.columns:
        print("❌ 'Symbol' column not found in data.")
        return

    symbols = df["Symbol"].unique()
    for symbol in symbols:
        subset = df[df["Symbol"] == symbol]
        plt.figure(figsize=(10, 5))
        plt.plot(subset["Date"], subset["Close"], label="Close Price", marker='o')
        plt.plot(subset["Date"], subset["Open"], label="Open Price", linestyle='--')
        plt.title(f"{symbol} Stock Trend")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Main Execution
if __name__ == "__main__":
    excel_file = get_excel_file()
    if excel_file and os.path.exists(excel_file):
        df_raw = load_excel_data(excel_file)
        if df_raw is not None:
            df_clean = preprocess_data(df_raw)
            save_to_database(df_clean)  # Save to MySQL
            plot_stock_trends(df_clean)  # Plot the data
        else:
            print("Failed to read the Excel file.")
    else:
        print("No file selected or file not found.")
