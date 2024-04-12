-- Inserció de dades a la taula statuses
INSERT INTO statuses (id, name, slug) VALUES
(1, 'Nou', 'nou');

-- Reiniciar la seqüència d'autoincrement per a la taula statuses a 1 (MySQL no utilitza la taula SQLITE_SEQUENCE)
ALTER TABLE statuses AUTO_INCREMENT = 2;

-- Inserció de dades a la taula categories
INSERT INTO categories (id, name, slug) VALUES
(1, 'Electrònica', 'electronica'),
(2, 'Roba', 'roba'),
(3, 'Joguines', 'joguines');

-- Reiniciar la seqüència d'autoincrement per a la taula categories a 4 (MySQL no utilitza la taula SQLITE_SEQUENCE)
ALTER TABLE categories AUTO_INCREMENT = 4;

-- Inserció de dades a la taula users
INSERT INTO users (id, name, email, role, verified, password) VALUES
(1, 'Joan Pérez', 'joan@example.com', 'admin', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(2, 'Anna García', 'anna@example.com', 'moderator', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(3, 'Elia Rodríguez', 'elia@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
(4, 'Kevin Salardú', 'kevin@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');

-- Reiniciar la seqüència d'autoincrement per a la taula users a 5 (MySQL no utilitza la taula SQLITE_SEQUENCE)
ALTER TABLE users AUTO_INCREMENT = 5;

-- Inserció de dades fictícies a la taula products
INSERT INTO products (id, title, description, photo, price, category_id, status_id, seller_id) VALUES
(1, 'Telèfon mòbil', 'Un telèfon intel·ligent d''última generació.', 'no_image.png', 599.99, 1, 1, 3),
(2, 'Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 1, 3),
(3, 'Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 1, 4);

-- Reiniciar la seqüència d'autoincrement per a la taula products a 4 (MySQL no utilitza la taula SQLITE_SEQUENCE)
ALTER TABLE products AUTO_INCREMENT = 4;
