books_authors_inner = '''
select
	b.title,
	a.first_name,
	a.last_name
from books b
inner join authors a on a.id = b.author_id
'''

books_authors_left = '''
select
	b.title,
	a.first_name,
	a.last_name
from authors a
left join books b on a.id = b.author_id
'''

books_authors_outer = '''
select
	b.title,
	a.first_name,
	a.last_name
from authors a
right join books b on a.id = b.author_id
'''

book_sales_inner = '''
select
	b.title,
	a.first_name,
	a.last_name,
	s.quantity
from books b
inner join authors a on a.id = b.author_id
inner join sales s on b.id = s.book_id
'''

all_book_sales_left = '''
select
	b.title,
	a.first_name,
	a.last_name,
	s.quantity
from books b
full join authors a on a.id = b.author_id
left join sales s on b.id = s.book_id
'''

sum_book_sold_inner = '''
select
	b.title,
	a.first_name,
	a.last_name,
	sum(s.quantity) as quantity
from books b
inner join authors a on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by b.title, a.first_name, a.last_name
'''

sum_book_sold_all_authors_left = '''
select
	b.title,
	a.first_name,
	a.last_name,
	sum(s.quantity) as quantity
from books b
inner join authors a on a.id = b.author_id
left join sales s on b.id = s.book_id
group by b.title, a.first_name, a.last_name
'''

max_book_sold = '''
with sales_statistics as (
	select
		a.first_name,
		a.last_name,
		sum(s.quantity) as quantity
	from sales s
	join books b on	b.id = s.book_id
	join authors a on a.id = b.author_id
	group by a.first_name, a.last_name
)

select *
from sales_statistics
where quantity in (select max(quantity) from sales_statistics)
'''

more_than_avg_book_sold = '''
with sales_statistics as (
	select
		a.first_name,
		a.last_name,
		sum(s.quantity) as quantity
	from sales s
	join books b on	b.id = s.book_id
	join authors a on a.id = b.author_id
	group by a.first_name, a.last_name
)

select *
from sales_statistics
where quantity > (select avg(quantity) from sales_statistics)
'''
