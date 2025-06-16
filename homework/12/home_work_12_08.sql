-- Select book names with authors using inner join

select
	b.title,
	a.first_name,
	a.last_name
from books b
inner join authors a on a.id = b.author_id;


-- Select book names with ALL authors using left join

select
	b.title,
	a.first_name,
	a.last_name
from authors a
left join books b on a.id = b.author_id;


-- Select ALL book names with authors using right join

select
	b.title,
	a.first_name,
	a.last_name
from authors a
right join books b on a.id = b.author_id;


-- Select book names with authors and sales quontities using inner join

select
	b.title,
	a.first_name,
	a.last_name,
	s.quantity
from books b
inner join authors a on a.id = b.author_id
inner join sales s on b.id = s.book_id; 


-- Select ALL book names with ALL authors and sales quontities using left join

select
	b.title,
	a.first_name,
	a.last_name,
	s.quantity
from books b
full join authors a on a.id = b.author_id
left join sales s on b.id = s.book_id; 


-- Select sum of sold books of each author susing inner join

select
	b.title,
	a.first_name,
	a.last_name,
	sum(s.quantity) as quantity
from books b
inner join authors a on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by b.title, a.first_name, a.last_name; 


-- Select sum of sold books of ALL authors susing left join

select
	b.title,
	a.first_name,
	a.last_name,
	sum(s.quantity) as quantity
from books b
inner join authors a on a.id = b.author_id
left join sales s on b.id = s.book_id
group by b.title, a.first_name, a.last_name; 


-- Select author of most selling book using subqueries and joins

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
where quantity in (select max(quantity) from sales_statistics);


-- Select books sold more than average using subqueries and joins

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
where quantity > (select avg(quantity) from sales_statistics);