CREATE DATABASE `librarydb`;
USE `librarydb`;
CREATE TABLE `librarydb`.`books` ( 
    `id` INT(11) NOT NULL AUTO_INCREMENT , 
    `title` VARCHAR(255) NOT NULL , 
    `author` VARCHAR(255) NOT NULL , 
    `average_rating` FLOAT NULL , 
    `isbn` VARCHAR(10) NOT NULL UNIQUE, 
    `isbn13` VARCHAR(13) NOT NULL UNIQUE, 
    `language_code` VARCHAR(3), 
    `num_pages` INT(5), 
    `ratings_count` INT(11), 
    `text_reviews_count` INT(11), 
    `publication_date` DATE NOT NULL , 
    `publisher` VARCHAR(255) NOT NULL , 
    `total_quantity` INT(11) NOT NULL , 
    `available_quantity` INT(11) NOT NULL , 
    `rented_count` INT(11) NOT NULL DEFAULT 0, 
    PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `librarydb`.`members` ( 
    `id` INT(11) NOT NULL AUTO_INCREMENT , 
    `name` VARCHAR(100) NOT NULL , 
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `registered_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    `outstanding_debt` FLOAT NOT NULL DEFAULT 0, 
    `amount_spent` FLOAT NOT NULL DEFAULT 0, 
    PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `librarydb`.`transactions` ( 
    `id` INT(11) NOT NULL AUTO_INCREMENT , 
    `book_id` INT(11) NOT NULL , 
    `member_id` INT(11) NOT NULL , 
    `per_day_fee` FLOAT NOT NULL , 
    `borrowed_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    `returned_on` TIMESTAMP NULL , 
    `total_charge` FLOAT NULL , 
    `amount_paid` FLOAT NULL , 
    PRIMARY KEY (`id`),
    FOREIGN KEY (`book_id`) REFERENCES books(`id`),
    FOREIGN KEY (`member_id`) REFERENCES members(`id`)) ENGINE = InnoDB;



CREATE TABLE `librarydb`.`digitalbooks` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `author` VARCHAR(100) NOT NULL,
    `publisher` VARCHAR(255) NOT NULL,
    `cost` FLOAT NOT NULL,
    `access_link` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE `librarydb`.`purchases` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `member_id` INT(11) NOT NULL,
    `digitalbook_id` INT(11) NOT NULL,
    `purchase_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `total_cost` FLOAT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`member_id`) REFERENCES members(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`digitalbook_id`) REFERENCES digitalbooks(`id`) ON DELETE CASCADE
) ENGINE = InnoDB;

ALTER TABLE purchases ADD COLUMN access_token VARCHAR(255) NOT NULL;
ALTER TABLE purchases ADD COLUMN expires_at DATETIME NOT NULL;
