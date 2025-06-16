-- Create books table

create table books (
	id SERIAL primary key,
	title varchar(100),
	author_id int references authors(id),
	publication_year int
);
