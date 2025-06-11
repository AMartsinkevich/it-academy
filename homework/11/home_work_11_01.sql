-- Create Employees table with "Name", "Position", "Department", "Salary" columns.

create table employees (
	id SERIAL primary key,
	name text,
	position text,
	department text,
	salary numeric(10, 2)
);
