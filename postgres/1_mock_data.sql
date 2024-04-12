-- Inserció de dades a la taula statuses
INSERT INTO statuses (name, slug) VALUES
('Nou', 'nou');

-- Inserció de dades a la taula categories
INSERT INTO categories (name, slug) VALUES
('Electrònica', 'electronica'),
('Roba', 'roba'),
('Joguines', 'joguines');

-- Inserció de dades a la taula users
INSERT INTO users (name, email, role, verified, password) VALUES
('Joan Pérez', 'joan@example.com', 'admin', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
('Anna García', 'anna@example.com', 'moderator', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
('Elia Rodríguez', 'elia@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4'),
('Kevin Salardú', 'kevin@example.com', 'wanner', TRUE, 'scrypt:32768:8:1$lwqNpblQ9OiKBfeM$4d63ebdf494cc8e363f14494bca1c5246f6689b45904431f69fbcb535b7e41bd012e9b41c850125d7f8b790cb320579a46427b69eda892517669eba0244b77b4');

-- Inserció de dades fictícies a la taula products
INSERT INTO products (title, description, photo, price, category_id, status_id, seller_id) VALUES
('Telèfon mòbil', 'Un telèfon intel·ligent d''última generació.', 'no_image.png', 599.99, 1, 1, 3),
('Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 1, 3),
('Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 1, 4);
