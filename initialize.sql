DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at DATETIME
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, created_at)
VALUES (1, 'alice', 'alice@example.com', '2026-01-10 09:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (2, 'bob', 'bob@example.com', '2026-01-11 10:30:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (3, 'charlie', 'charlie@example.com', '2026-01-12 11:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (4, 'diana', 'diana@example.com', '2026-01-13 12:15:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (5, 'ethan', 'ethan@example.com', '2026-01-14 13:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (6, 'fiona', 'fiona@example.com', '2026-01-15 14:30:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (7, 'george', 'george@example.com', '2026-01-16 15:45:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (8, 'hannah', 'hannah@example.com', '2026-01-17 16:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (9, 'ian', 'ian@example.com', '2026-01-18 17:20:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES (10, 'julia', 'julia@example.com', '2026-01-19 18:00:00');


INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (1, 1, 'My First Post', 'Hello everyone!', '2026-02-01 09:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (2, 2, 'Learning SQL', 'I am learning how to use SQL databases.', '2026-02-02 10:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (3, 3, 'Data Science', 'Data science is really interesting.', '2026-02-03 11:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (4, 4, 'College Life', 'I had a great day at college today.', '2026-02-04 12:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (5, 5, 'Python', 'Python is one of my favorite programming languages.', '2026-02-05 13:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (6, 6, 'Database Practice', 'Today I practiced creating tables.', '2026-02-06 14:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (7, 7, 'Projects', 'I am working on a new programming project.', '2026-02-07 15:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (8, 8, 'Weekend Plans', 'Looking forward to the weekend!', '2026-02-08 16:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (9, 9, 'Technology', 'Technology continues to change quickly.', '2026-02-09 17:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (10, 10, 'Hello SQL', 'This is my tenth post.', '2026-02-10 18:00:00');