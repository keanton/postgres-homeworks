"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

class data_base:
    def __init__(self, db_name, password, user='postgres'):
        """
        :param db_name: Название базы данных
        :param user: Имя пользователя (администратора бд) (default = postgres)
        :param password: Пароль
        """
        self.connection = psycopg2.connect(host='localhost', database=db_name,
                              user=user, password=password)
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True

    def table_insert(self, from_file='', table_name=''):
        """
        :param from_file: Файл от куда берутся данные для бд,
        расположение должно быть в папке north_data (example: customers_data.csv)
        :param table_name: Название таблицы, куда будут вноситься данные

        В ДАННЫЙ МОМЕНТ НЕ ИСПОЛЬЗУЕТСЯ
        """

        with open(f'north_data/{from_file}') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for i in csv_file:
                val = i[0], i[1], i[2]
                if table_name.lower() == 'orders' or table_name == 'employees':
                    print(f'Добавляем в таблицу {table_name} - {i}')
                    self.cursor.execute(f'INSERT INTO {table_name.lower()} '
                                        f'VALUES {i[0], i[1], i[2], i[3], i[4]}')
                    self.connection.commit()
                elif table_name.lower() == 'customers':
                    print(f'Добавляем в таблицу Customers {i}')
                    self.cursor.execute(f'INSERT INTO customers(customer_id, customer_name, customer_contact) '
                                        f'VALUES(%s, %s, %s)', (val))
                    self.connection.commit()
                else:
                    raise Exception(f'Такой таблицы не существует.')

    #  Отдельные функции добавления
    def table_insert_emp(self):
        with open(f'north_data/employees_data.csv') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for i in csv_file:
                val = i[0], i[1], i[2], i[3], i[4]
                self.cursor.execute(f'INSERT INTO employees(emp_first_name,emp_last_name,emp_title,emp_birtday,notes)'
                                    f'VALUES(%s,%s,%s,%s,%s)', val)
                self.connection.commit()

    def table_insert_customers(self):
        with open(f'north_data/customers_data.csv') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for i in csv_file:
                self.cursor.execute(f'INSERT INTO customers VALUES {i[0], i[1], i[2]}')
                self.connection.commit()

    def table_insert_orders(self):
        with open(f'north_data/orders_data.csv') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for i in csv_file:
                val = i[0], i[1], i[2], i[3], i[4]
                self.cursor.execute(f'INSERT INTO orders(order_id, order_customer, '
                                    f'order_emp_id, order_date, order_destination '
                                    f'VALUES(%s, %s, %s, %s, %s)', val)
                self.connection.commit()


if __name__ == '__main__':
    db = data_base('north', '5772')
    db.table_insert('customers_data.csv', 'customers')
    db.table_insert('employees_data.csv', 'employees')
    db.table_insert('orders_data.csv', 'orders')
