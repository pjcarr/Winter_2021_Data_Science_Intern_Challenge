"""
shoe_sales_analysis.py

Reads in .xlsx file containing shoe sales data. Calculates the cost per shoe from
the order total divided by the number of items. Extracts sales data within the
95th percentile, then determines the average order value by taking the mean
order amount.
"""
import pandas as pd
import numpy as np


def main():
    """
    main data cleaning and analysis function
    """
    # read in the .xlsx file
    shoe_sales = pd.read_excel("shoe sales.xlsx", sheet_name="Sheet1")

    # calculate the price per shoe by dividing the total amount of an order by the
    # number of items in the order
    price_per_shoe = shoe_sales["order_amount"] / shoe_sales["total_items"]

    # inserting the price per shoe series into the shoe sales dataframe
    shoe_sales["price_per_shoe"] = price_per_shoe

    # calculating the value of the 95th percentile for the price per shoe
    pps_95 = np.percentile(shoe_sales["price_per_shoe"], 95)

    # calculating the 95th percentile for the number of items in an order
    total_items_95 = np.percentile(shoe_sales["total_items"], 95)

    # exctracting all sales within the 95th percentile for number of items
    shoe_sales_ti95 = shoe_sales[shoe_sales["total_items"] < total_items_95]

    # extracting all sales within the 95th percentile for the shoe cost
    shoe_sales_95 = shoe_sales_ti95[shoe_sales_ti95["price_per_shoe"] < pps_95]

    # reporting the average order value as the mean of the cleaned order amount
    aov = shoe_sales_95["order_amount"].mean()
    print(f"""The average order value is ${aov:.2f} excluding orders
of more than {int(total_items_95)} shoes and orders where the shoes cost
more than ${pps_95:.2f}""")

if __name__ == '__main__':
    main()
