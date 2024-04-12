INSERT INTO statuses (id, name, slug) VALUES
(1, 'Nou', 'nou');
UPDATE SQLITE_SEQUENCE SET seq = 1 WHERE name = 'statuses';

INSERT INTO categories (id, name, slug) VALUES
(1, 'Electrònica', 'electronica'),
(2, 'Roba', 'roba'),
(3, 'Joguines', 'joguines');
UPDATE SQLITE_SEQUENCE SET seq = 3 WHERE name = 'categories';

-- Les contrasenyes són test
INSERT INTO users (id, name, email, role, verified, password) VALUES
(1, 'Joan Pérez', 'joan@example.com', 'admin', TRUE, 'pbkdf2:sha256:600000$Fv0iPjfkIXY5TzS6$62c0450779c89ec8605cb7239e2fe9079b94b8ca79526dfd4ea3261b437ae334'),
(2, 'Anna García', 'anna@example.com', 'moderator', TRUE, 'pbkdf2:sha256:600000$Fv0iPjfkIXY5TzS6$62c0450779c89ec8605cb7239e2fe9079b94b8ca79526dfd4ea3261b437ae334'),
(3, 'Elia Rodríguez', 'elia@example.com', 'wanner', TRUE, 'pbkdf2:sha256:600000$Fv0iPjfkIXY5TzS6$62c0450779c89ec8605cb7239e2fe9079b94b8ca79526dfd4ea3261b437ae334'),
(4, 'Kevin Salardú', 'kevin@example.com', 'wanner', TRUE, 'pbkdf2:sha256:600000$Fv0iPjfkIXY5TzS6$62c0450779c89ec8605cb7239e2fe9079b94b8ca79526dfd4ea3261b437ae334');
UPDATE SQLITE_SEQUENCE SET seq = 4 WHERE name = 'users';

-- Inserir dades fictícies a la taula products
INSERT INTO products (id, title, description, photo, price, category_id, status_id, seller_id) VALUES
(1, 'Telèfon mòbil', 'Un telèfon intel·ligent d''última generació.', 'no_image.png', 599.99, 1, 1, 3),
(2, 'Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 1, 3),
(3, 'Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 1, 4);
UPDATE SQLITE_SEQUENCE SET seq = 3 WHERE name = 'products';