-- SQL-команды для создания таблиц
CREATE table employees
(
	emp_first_name varchar(100) NOT NULL,
	emp_last_name varchar(100) NOT NULL,
	emp_title varchar(100) NOT NULL,
	emp_birtday varchar(30) NOT NULL,
	notes varchar (999)
);

CREATE table orders
(
	order_id int PRIMARY KEY,
	order_customer varchar(50) NOT NULL,
	order_emp_id int NOT NULL,
	order_date varchar(30) NOT NULL,
	order_destination varchar(150) NOT NULL
);

CREATE table customers
(
    customer_id varchar(20) NOT NULL,
	customer_name varchar(100) NOT NULL,
	customer_contact varchar(50) NOT NULL
)