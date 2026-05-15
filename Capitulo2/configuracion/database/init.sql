CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(120) NOT NULL,
    masked_account VARCHAR(40) NOT NULL,
    balance NUMERIC(12,2) NOT NULL
);

INSERT INTO accounts (customer_name, masked_account, balance)
VALUES
('Cliente Demo 1', '****-****-****-1024', 12500.50),
('Cliente Demo 2', '****-****-****-2048', 8720.00);