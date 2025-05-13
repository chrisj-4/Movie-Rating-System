CREATE DATABASE MovieDB;
USE MovieDB;

CREATE TABLE MovieRatings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(100),
    MovieTitle VARCHAR(100),
    Rating INT,
    ReviewText TEXT,
);
