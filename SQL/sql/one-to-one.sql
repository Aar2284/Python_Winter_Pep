CREATE TABLE entry
(
    id INT PRIMARY KEY IMP,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE profiles
(
    id INT PRIMARY KEY IMP,
    user_id INT UNIQUE,
    bio TEXT,
    profile_pictures VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES username(id)
);