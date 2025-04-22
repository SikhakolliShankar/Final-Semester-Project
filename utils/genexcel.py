import pandas as pd

# Sample data for the `books` table
books_data = [
    {
        "title": "To Kill a Mockingbird", "author": "Harper Lee", "average_rating": 4.27, "isbn": "0061120081",
        "isbn13": "9780061120084", "language_code": "eng", "num_pages": 324, "ratings_count": 4254034,
        "text_reviews_count": 91017, "publication_date": "2006-05-23", "publisher": "Harper Perennial Modern Classics",
        "genre": "Fiction", "total_quantity": 10, "available_quantity": 10, "rented_count": 0
    },
    {
        "title": "1984", "author": "George Orwell", "average_rating": 4.17, "isbn": "0451524934",
        "isbn13": "9780451524935", "language_code": "eng", "num_pages": 328, "ratings_count": 3101383,
        "text_reviews_count": 70748, "publication_date": "1950-07-01", "publisher": "Signet Classic",
        "genre": "Dystopia", "total_quantity": 15, "available_quantity": 15, "rented_count": 0
    },
    {
        "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "average_rating": 3.91, "isbn": "0743273567",
        "isbn13": "9780743273565", "language_code": "eng", "num_pages": 180, "ratings_count": 3895620,
        "text_reviews_count": 64024, "publication_date": "2004-09-30", "publisher": "Scribner",
        "genre": "Classic", "total_quantity": 8, "available_quantity": 8, "rented_count": 0
    },
    {
        "title": "Pride and Prejudice", "author": "Jane Austen", "average_rating": 4.26, "isbn": "0141439513",
        "isbn13": "9780141439518", "language_code": "eng", "num_pages": 279, "ratings_count": 3071964,
        "text_reviews_count": 63628, "publication_date": "2002-12-31", "publisher": "Penguin Classics",
        "genre": "Romance", "total_quantity": 12, "available_quantity": 12, "rented_count": 0
    },
    {
        "title": "The Catcher in the Rye", "author": "J.D. Salinger", "average_rating": 3.8, "isbn": "0316769487",
        "isbn13": "9780316769488", "language_code": "eng", "num_pages": 277, "ratings_count": 2750901,
        "text_reviews_count": 59255, "publication_date": "2001-01-30", "publisher": "Little, Brown and Company",
        "genre": "Fiction", "total_quantity": 10, "available_quantity": 10, "rented_count": 0
    },
    {
        "title": "The Hobbit", "author": "J.R.R. Tolkien", "average_rating": 4.28, "isbn": "0345339681",
        "isbn13": "9780345339683", "language_code": "eng", "num_pages": 300, "ratings_count": 3071609,
        "text_reviews_count": 65308, "publication_date": "1986-07-12", "publisher": "Del Rey",
        "genre": "Fantasy", "total_quantity": 14, "available_quantity": 14, "rented_count": 0
    },
    {
        "title": "Fahrenheit 451", "author": "Ray Bradbury", "average_rating": 3.99, "isbn": "1451673310",
        "isbn13": "9781451673319", "language_code": "eng", "num_pages": 249, "ratings_count": 1698057,
        "text_reviews_count": 30736, "publication_date": "2012-01-10", "publisher": "Simon & Schuster",
        "genre": "Science Fiction", "total_quantity": 9, "available_quantity": 9, "rented_count": 0
    },
    {
        "title": "Moby-Dick", "author": "Herman Melville", "average_rating": 3.49, "isbn": "1503280780",
        "isbn13": "9781503280786", "language_code": "eng", "num_pages": 654, "ratings_count": 480914,
        "text_reviews_count": 10045, "publication_date": "2014-11-06", "publisher": "CreateSpace",
        "genre": "Adventure", "total_quantity": 5, "available_quantity": 5, "rented_count": 0
    },
    {
        "title": "Jane Eyre", "author": "Charlotte Brontë", "average_rating": 4.13, "isbn": "0141441143",
        "isbn13": "9780141441146", "language_code": "eng", "num_pages": 532, "ratings_count": 1671623,
        "text_reviews_count": 36618, "publication_date": "2006-04-27", "publisher": "Penguin Classics",
        "genre": "Gothic", "total_quantity": 11, "available_quantity": 11, "rented_count": 0
    },
    {
        "title": "The Book Thief", "author": "Markus Zusak", "average_rating": 4.39, "isbn": "0375842209",
        "isbn13": "9780375842207", "language_code": "eng", "num_pages": 552, "ratings_count": 1892636,
        "text_reviews_count": 103234, "publication_date": "2007-09-11", "publisher": "Knopf Books for Young Readers",
        "genre": "Historical", "total_quantity": 13, "available_quantity": 13, "rented_count": 0
    }
]

# Create DataFrame
books_df = pd.DataFrame(books_data)

# Save to Excel file
books_file_path = "books.xlsx"
books_df.to_excel(books_file_path, index=False)

books_file_path
