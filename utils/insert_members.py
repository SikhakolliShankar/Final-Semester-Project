import pandas as pd
# import MySQL
import pymysql
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import get_db_connection

 
def insert_members_from_excel(file_path):
    try:
        # Read Excel file using pandas
        df = pd.read_excel(file_path,engine="openpyxl")

        # Check for required columns
        if 'name' not in df.columns or 'email' not in df.columns:
            print("Excel file must contain 'name' and 'email' columns.")
            return

        # Connect to the MySQL database
        connection = get_db_connection()

        cursor = connection.cursor()

        insert_query = """
            INSERT INTO members (name, email)
            VALUES (%s, %s)
        """

        # Iterate through the DataFrame and insert each row
        for _, row in df.iterrows():
            try:
                cursor.execute(insert_query, (row['name'], row['email']))
            except Exception as e:
                print(f"Skipping duplicate email: ", e)

        # Commit and close connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Members inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")
insert_members_from_excel("members_data.xlsx")
