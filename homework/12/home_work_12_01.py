import os
import psycopg2
import sql

DB_NAME='home_work_12'
DB_USER = 'postgres'
DB_PASS = os.environ['DB_PASS']

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS)


if __name__ == "__main__":
    with conn.cursor() as cur:
        print('\nSelect book names with authors using inner join:')
        cur.execute(sql.books_authors_inner)
        for row in cur:
            print(row)

        print('\nSelect book names with ALL authors using left join:')
        cur.execute(sql.books_authors_left)
        for row in cur:
            print(row)

        print('\nSelect ALL book names with authors using right join:')
        cur.execute(sql.books_authors_left)
        for row in cur:
            print(row)

        print('\nSelect book names with authors and sales quontities using inner join:')
        cur.execute(sql.book_sales_inner)
        for row in cur:
            print(row)

        print('\nSelect ALL book names with ALL authors and sales quontities using left join:')
        cur.execute(sql.all_book_sales_left)
        for row in cur:
            print(row)

        print('\nSelect sum of sold books of each author susing inner join:')
        cur.execute(sql.sum_book_sold_inner)
        for row in cur:
            print(row)

        print('\nSelect sum of sold books of ALL authors susing left join:')
        cur.execute(sql.sum_book_sold_all_authors_left)
        for row in cur:
            print(row)

        print('\nSelect author of most selling book using subqueries and joins:')
        cur.execute(sql.max_book_sold)
        for row in cur:
            print(row)

        print('\nSelect books sold more than average using subqueries and joins:')
        cur.execute(sql.more_than_avg_book_sold)
        for row in cur:
            print(row)
