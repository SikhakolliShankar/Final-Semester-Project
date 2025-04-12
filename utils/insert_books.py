import pandas as pd
import pymysql
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import get_db_connection

def insert_books_from_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')

        required_columns = [
            'title', 'author', 'isbn', 'isbn13', 'publication_date', 'publisher',
            'genre', 'total_quantity', 'available_quantity'
        ]
        for col in required_columns:
            if col not in df.columns:
                print(f"Missing required column: {col}")
                return

        # Convert columns to proper formats
        df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')
        df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
        df['isbn'] = df['isbn'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else None)
        df['isbn13'] = df['isbn13'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else None)

        # Replace NaN with None for SQL NULL compatibility
        df = df.where(pd.notnull(df), None)

        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO books (
                title, author, average_rating, isbn, isbn13, language_code,
                num_pages, ratings_count, text_reviews_count, publication_date,
                publisher, genre, total_quantity, available_quantity, rented_count
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            try:
                cursor.execute(insert_query, (
                    row['title'],
                    row['author'],
                    row.get('average_rating'),
                    row['isbn'],
                    row['isbn13'],
                    row.get('language_code'),
                    row.get('num_pages'),
                    row.get('ratings_count'),
                    row.get('text_reviews_count'),
                    row['publication_date'].strftime('%Y-%m-%d') if pd.notnull(row['publication_date']) else None,
                    row['publisher'],
                    row['genre'],
                    row['total_quantity'],
                    row['available_quantity'],
                    row.get('rented_count', 0)
                ))
            except Exception as e:
                print(f"Skipping book with ISBN {row.get('isbn')} due to error: {e}")

        connection.commit()
        cursor.close()
        connection.close()
        print("Books inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
insert_books_from_excel("books_data.xlsx")
