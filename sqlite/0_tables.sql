CREATE TABLE categories (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	slug TEXT NOT NULL UNIQUE
);

CREATE TABLE statuses (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE,
	slug TEXT UNIQUE
);

CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	role TEXT NOT NULL,
	password TEXT NOT NULL,
	email_token TEXT DEFAULT NULL,
	verified INTEGER NOT NULL DEFAULT FALSE, -- SQLite no té booleans
	auth_token TEXT DEFAULT NULL,
    auth_token_expiration DATETIME DEFAULT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	updated DATETIME NOT NULL DEFAULT (DATETIME('now'))
);

CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	photo TEXT NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	category_id INTEGER NOT NULL,
	status_id INTEGER NOT NULL,
	seller_id INTEGER NOT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	updated DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY (category_id) REFERENCES categories(id),
	FOREIGN KEY (status_id) REFERENCES statuses(id),
	FOREIGN KEY (seller_id) REFERENCES users(id)
);

CREATE TABLE blocked_users (
	user_id INTEGER PRIMARY KEY,
	message TEXT NOT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE banned_products (
	product_id INTEGER PRIMARY KEY,
	reason TEXT NOT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_id INTEGER NOT NULL,
	buyer_id INTEGER NOT NULL,
	offer DECIMAL(10, 2) NOT NULL,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	CONSTRAINT uc_product_buyer UNIQUE (product_id, buyer_id),
	FOREIGN KEY (product_id) REFERENCES products(id),
	FOREIGN KEY (buyer_id) REFERENCES users(id)
);

CREATE TABLE confirmed_orders (
	order_id INTEGER PRIMARY KEY,
	created DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY (order_id) REFERENCES orders(id)
);
