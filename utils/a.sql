use librarydb;
-- ALTER TABLE books ADD COLUMN genre VARCHAR(100) AFTER publisher;

-- UPDATE books SET genre = 'Comedy' WHERE title in ('ABC','AAA','DEF');
-- UPDATE books SET genre = 'Drama' WHERE title in ('we','as', 'Outlander');
ALTER TABLE books MODIFY average_rating FLOAT NULL;

-- ALTER TABLE books 
-- MODIFY COLUMN language_code VARCHAR(3);

-- ALTER TABLE books 
-- MODIFY COLUMN num_pages INT(5);

-- ALTER TABLE books 
-- MODIFY COLUMN ratings_count INT(11);

-- ALTER TABLE books 
-- MODIFY COLUMN text_reviews_count INT(11);

-- ALTER TABLE purchases ADD COLUMN access_token VARCHAR(255) NOT NULL;
-- ALTER TABLE purchases ADD COLUMN expires_at DATETIME NOT NULL;
