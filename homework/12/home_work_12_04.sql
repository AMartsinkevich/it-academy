-- Create sales table

create table sales (
	id SERIAL primary key,
	book_id int references books(id),
	quantity int
);
