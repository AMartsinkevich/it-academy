create_database = '''
create database transport
'''
create_table_passengers = '''
create table passengers (
	id SERIAL primary key,
	name varchar(100),
	passport varchar(100) UNIQUE
)
'''
create_type_transpotr = '''
CREATE TYPE transport_type AS ENUM ('bus', 'train', 'plane')
'''
create_table_transport = '''
create table transport (
	id SERIAL primary key,
	type transport_type,
	model_or_route varchar(100),
	capacity int
)
'''

create_table_bookings = '''
create table bookings (
	id SERIAL primary key,
	passenger_id int references passengers(id),
	transport_id int references transport(id),
	seat int,
	date date
)
'''
insert_passengers = '''
insert into passengers (name, passport)
values
	('Bob Gubka', 'AP12356789'),
	('Jingle Bells', 'PP213654789'),
	('Great Again', 'AA523641789'),
	('Like Me', 'FF000000000')
'''

insert_transport = '''
insert into transport (type, model_or_route, capacity)
values
	('bus', '123', 50),
	('bus', '73', 48),
	('bus', '24', 36),
	('bus', '26', 36),
	('bus', '142', 50),
	('train', '10', 100),
	('train', '11', 110),
	('train', '12', 120),
	('plane', 'Airbus 777', 360),
	('plane', 'Aerobus 217', 210),
	('plane', 'FlyTy 1515', 240),
	('plane', 'SpaceX 001', 10),
	('plane', 'SpaceX 007', 120)
'''

insert_bookings = '''
insert into bookings (passenger_id, transport_id, seat, date)
values
	(1, 1, 1, '2024-02-01'),
	(2, 1, 2, '2024-02-01'),
	(3, 1, 3, '2024-02-01'),
	(1, 2, 1, '2024-02-02'),
	(2, 2, 2, '2024-02-02'),
	(3, 2, 3, '2024-02-02'),
	(1, 3, 1, '2024-02-03'),
	(2, 3, 2, '2024-02-03'),
	(3, 3, 3, '2024-02-03'),
	(1, 4, 1, '2024-02-04'),
	(2, 4, 2, '2024-02-04'),
	(3, 4, 3, '2024-02-04'),
	(1, 5, 1, '2024-02-05'),
	(2, 5, 2, '2024-02-05'),
	(3, 5, 3, '2024-02-05'),

	(1, 6, 1, '2024-02-11'),
	(2, 6, 2, '2024-02-11'),
	(3, 6, 3, '2024-02-11'),
	(1, 7, 1, '2024-02-12'),
	(2, 7, 2, '2024-02-12'),
	(3, 7, 3, '2024-02-12'),
	(1, 8, 1, '2024-02-13'),
	(2, 8, 2, '2024-02-13'),
	(3, 8, 3, '2024-02-13'),

	(1, 9, 1, '2024-02-21'),
	(2, 9, 2, '2024-02-21'),
	(3, 9, 3, '2024-02-21'),
	(1, 10, 1, '2024-02-22'),
	(2, 10, 2, '2024-02-22'),
	(3, 10, 3, '2024-02-22'),
	(1, 11, 1, '2024-02-23'),
	(2, 11, 2, '2024-02-23'),
	(3, 11, 3, '2024-02-23'),
	(1, 12, 1, '2024-02-24'),
	(2, 12, 2, '2024-02-24'),
	(3, 12, 3, '2024-02-24'),
	(1, 13, 1, '2024-02-25'),
	(2, 13, 2, '2024-02-25'),
	(3, 13, 3, '2024-02-25')
'''
find_booked_passengers = '''
select
	p.name
from passengers p
where p.id in (
	select distinct
		b.passenger_id
	from bookings b
	)
'''
count_booked_seats = '''
select t.type, t.model_or_route, count(*) as booked_seats from bookings b
join transport t on t.id = b.transport_id
group by b.transport_id, t.type, t.model_or_route 
'''

find_passengers_by_date = '''
select p.name, p.passport, b.date from bookings b
join passengers p on p.id = b.passenger_id
where b.date = '2024-02-12'
'''

find_top_booked_transport = '''
select t.type, count(*) as bookings from bookings b 
join transport t on t.id = b.transport_id
group by t.type
order by bookings desc
limit 1
'''

find_free_seats = '''
select (40 - count(*)) as free_seats from bookings b
where b.transport_id = 1
'''

find_all_books = '''
select p.name, p.passport, t.type, b.seat, b.date from bookings b
join passengers p on p.id = b.passenger_id
join transport t on t.id = b.transport_id
'''
find_passengers_on_train = '''
select p.name, b.date from bookings b
join passengers p on p.id = b.passenger_id
where b.transport_id in (select id from transport where type = 'train')
'''
find_non_unique_bookings = '''
select p.name, count(*) as bookings from bookings b
join passengers p on p.id = b.passenger_id
group by p.name
having count(*) > 1
'''

create_index_on_date = '''
CREATE INDEX date_idx ON bookings (date)
'''