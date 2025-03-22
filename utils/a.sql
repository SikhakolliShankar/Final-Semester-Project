use librarydb;
ALTER TABLE purchases ADD COLUMN access_token VARCHAR(255) NOT NULL;
ALTER TABLE purchases ADD COLUMN expires_at DATETIME NOT NULL;
