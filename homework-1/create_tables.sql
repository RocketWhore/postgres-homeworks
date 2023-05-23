-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name varchar(100) NOT NULL,
	lasr_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date DATE,
	notes text NOT NULL
);



CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) ,
	employee_id int ,
	order_date DATE,
	ship_city varchar(100) NOT NULL

);