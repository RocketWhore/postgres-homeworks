"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Ametist371'
)
with conn:
    with conn.cursor() as cur:
        # Работаем с таблицей customers
        csvfile = open('north_data/customers_data.csv', newline='', encoding='utf-8')
        customers = csv.DictReader(csvfile)
        for row in customers:
            # Заменяем недопустимый символ "'"
            if "'" in row['customer_id']:
                customer_id = row['customer_id'].replace("'", "''")
            else:
                customer_id = row['customer_id']
            if "'" in row['company_name']:
                company_name = row['company_name'].replace("'", "''")
            else:
                company_name = row['company_name']
            if "'" in row['contact_name']:
                contact_name = row['contact_name'].replace("'", "''")
            else:
                contact_name = row['contact_name']
            cur.execute(
                "INSERT INTO customers VALUES (%s, %s, %s)", (customer_id, company_name, contact_name))
            # cur.execute('SELECT * FROM customers')
            # rows = cur.fetchall()

            # for row in rows:
            #     print(row)

        csvfile1 = open('north_data/employees_data.csv', newline='', encoding='utf-8')
        employees = csv.DictReader(csvfile1)
        for row in employees:
            # Заменяем недопустимый символ "'"
            if "'" in row['first_name']:
                first_name = row['first_name'].replace("'", "''")
            else:
                first_name = row['first_name']
            if "'" in row['last_name']:
                last_name = row['last_name'].replace("'", "''")
            else:
                last_name = row['last_name']
            if "'" in row['title']:
                title = row['title'].replace("'", "''")
            else:
                title = row['title']
            if "'" in row['birth_date']:
                birth_date = row['birth_date'].replace("'", "''")
            else:
                birth_date = row['birth_date']
            if "'" in row['notes']:
                notes = row['notes'].replace("'", "''")
            else:
                notes = row['notes']
            cur.execute(
                "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, title, birth_date, notes))


        csvfile2 = open('north_data/employees_data.csv', newline='', encoding='utf-8')
        employees = csv.DictReader(csvfile1)
        for row in employees:
            # Заменяем недопустимый символ "'"
            if "'" in row['order_id']:
                order_id = row['order_id'].replace("'", "''")
            else:
                order_id = row['order_id']
            if "'" in row['customer_id']:
                customer_id = row['customer_id'].replace("'", "''")
            else:
                customer_id = row['customer_id']
            if "'" in row['employee_id']:
                employee_id = row['employee_id'].replace("'", "''")
            else:
                employee_id = row['employee_id']
            if "'" in row['order_date']:
                order_date = row['order_date'].replace("'", "''")
            else:
                order_date = row['order_date']
            if "'" in row['ship_city']:
                ship_city = row['ship_city'].replace("'", "''")
            else:
                ship_city = row['ship_city']
            cur.execute(
                "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (order_id, customer_id, employee_id, order_date, ship_city))

        csvfile.close()
        csvfile1.close()
        csvfile2.close()


conn.close()

