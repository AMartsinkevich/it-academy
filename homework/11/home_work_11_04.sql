-- Add column "HireDate" to Employees table.

alter table employees
add column hiredate date default now();
